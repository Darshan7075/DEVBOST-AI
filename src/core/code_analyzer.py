"""
Code Analyzer - Analyzes code for issues, complexity, and quality
"""

import ast
import re
from typing import Dict, List, Any
from dataclasses import dataclass, field


@dataclass
class Issue:
    """Represents a code issue"""
    line: int
    severity: str  # 'error', 'warning', 'info'
    category: str  # 'syntax', 'style', 'security', 'performance'
    message: str
    suggestion: str = ""


@dataclass
class Metrics:
    """Code metrics"""
    complexity: int = 0
    lines_of_code: int = 0
    maintainability: int = 100
    functions: int = 0
    classes: int = 0


@dataclass
class AnalysisResult:
    """Result of code analysis"""
    status: str  # 'success', 'error', 'warning'
    language: str
    issues: List[Issue] = field(default_factory=list)
    metrics: Metrics = field(default_factory=Metrics)


class CodeAnalyzer:
    """Analyzes code for various issues and metrics"""
    
    def __init__(self):
        self.supported_languages = ['python', 'javascript', 'typescript']
    
    def analyze(self, code: str, language: str = "python") -> AnalysisResult:
        """
        Analyze code and return results
        
        Args:
            code: Source code to analyze
            language: Programming language
            
        Returns:
            AnalysisResult with issues and metrics
        """
        if language not in self.supported_languages:
            raise ValueError(f"Unsupported language: {language}")
        
        if not code or not code.strip():
            return AnalysisResult(
                status="warning",
                language=language,
                issues=[Issue(
                    line=0,
                    severity="warning",
                    category="general",
                    message="Empty code provided",
                    suggestion="Add some code to analyze"
                )]
            )
        
        if language == "python":
            return self._analyze_python(code)
        else:
            return AnalysisResult(
                status="success",
                language=language,
                issues=[],
                metrics=Metrics()
            )
    
    def _analyze_python(self, code: str) -> AnalysisResult:
        """Analyze Python code"""
        issues = []
        metrics = Metrics()
        
        # Count lines
        lines = code.split('\n')
        metrics.lines_of_code = len([l for l in lines if l.strip() and not l.strip().startswith('#')])
        
        # Try to parse the code
        try:
            tree = ast.parse(code)
            
            # Count functions and classes
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    metrics.functions += 1
                    # Check for missing docstring
                    if not ast.get_docstring(node):
                        issues.append(Issue(
                            line=node.lineno,
                            severity="warning",
                            category="style",
                            message=f"Function '{node.name}' lacks docstring",
                            suggestion="Add a docstring to describe the function"
                        ))
                    
                    # Calculate complexity (simplified)
                    complexity = self._calculate_complexity(node)
                    if complexity > 10:
                        issues.append(Issue(
                            line=node.lineno,
                            severity="warning",
                            category="complexity",
                            message=f"Function '{node.name}' has high complexity: {complexity}",
                            suggestion="Consider breaking down into smaller functions"
                        ))
                    metrics.complexity = max(metrics.complexity, complexity)
                
                elif isinstance(node, ast.ClassDef):
                    metrics.classes += 1
            
            # Check for security issues
            security_issues = self._check_security(code)
            issues.extend(security_issues)
            
            # Check style issues
            style_issues = self._check_style(code)
            issues.extend(style_issues)
            
            status = "success" if not any(i.severity == "error" for i in issues) else "error"
            
        except SyntaxError as e:
            issues.append(Issue(
                line=e.lineno or 0,
                severity="error",
                category="syntax",
                message=f"Syntax error: {e.msg}",
                suggestion="Fix the syntax error"
            ))
            status = "error"
        
        # Calculate maintainability score
        if issues:
            error_count = sum(1 for i in issues if i.severity == "error")
            warning_count = sum(1 for i in issues if i.severity == "warning")
            metrics.maintainability = max(0, 100 - (error_count * 20) - (warning_count * 5))
        
        return AnalysisResult(
            status=status,
            language="python",
            issues=issues,
            metrics=metrics
        )
    
    def _calculate_complexity(self, node: ast.FunctionDef) -> int:
        """Calculate cyclomatic complexity (simplified)"""
        complexity = 1
        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.While, ast.For, ast.ExceptHandler)):
                complexity += 1
            elif isinstance(child, ast.BoolOp):
                complexity += len(child.values) - 1
        return complexity
    
    def _check_security(self, code: str) -> List[Issue]:
        """Check for common security issues"""
        issues = []
        lines = code.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Check for SQL injection risk
            if re.search(r'f["\'].*SELECT.*{.*}.*["\']', line, re.IGNORECASE):
                issues.append(Issue(
                    line=i,
                    severity="error",
                    category="security",
                    message="Potential SQL injection vulnerability",
                    suggestion="Use parameterized queries instead of string formatting"
                ))
            
            # Check for eval usage
            if 'eval(' in line:
                issues.append(Issue(
                    line=i,
                    severity="error",
                    category="security",
                    message="Use of eval() is dangerous",
                    suggestion="Avoid eval() or use ast.literal_eval() for safe evaluation"
                ))
            
            # Check for hardcoded passwords
            if re.search(r'password\s*=\s*["\'][^"\']+["\']', line, re.IGNORECASE):
                issues.append(Issue(
                    line=i,
                    severity="warning",
                    category="security",
                    message="Possible hardcoded password",
                    suggestion="Use environment variables or secure configuration"
                ))
        
        return issues
    
    def _check_style(self, code: str) -> List[Issue]:
        """Check for style issues"""
        issues = []
        lines = code.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Check line length
            if len(line) > 120:
                issues.append(Issue(
                    line=i,
                    severity="info",
                    category="style",
                    message=f"Line too long ({len(line)} > 120 characters)",
                    suggestion="Break line into multiple lines"
                ))
            
            # Check for multiple statements on one line
            if ';' in line and not line.strip().startswith('#'):
                issues.append(Issue(
                    line=i,
                    severity="warning",
                    category="style",
                    message="Multiple statements on one line",
                    suggestion="Put each statement on a separate line"
                ))
        
        return issues


def main():
    """Demo of code analyzer"""
    analyzer = CodeAnalyzer()
    
    # Example 1: Good code
    print("=" * 60)
    print("Example 1: Analyzing good code")
    print("=" * 60)
    good_code = '''
def calculate_sum(numbers):
    """Calculate the sum of a list of numbers"""
    return sum(numbers)
'''
    result = analyzer.analyze(good_code)
    print(f"Status: {result.status}")
    print(f"Issues found: {len(result.issues)}")
    print(f"Metrics: {result.metrics}")
    
    # Example 2: Code with issues
    print("\n" + "=" * 60)
    print("Example 2: Analyzing code with issues")
    print("=" * 60)
    bad_code = '''
def bad_function(x):
    if x > 0:
        if x > 10:
            if x > 20:
                return "very high"
            else:
                return "high"
        else:
            return "medium"
    else:
        return "low"

password = "hardcoded123"
query = f"SELECT * FROM users WHERE id = {user_id}"
'''
    result = analyzer.analyze(bad_code)
    print(f"Status: {result.status}")
    print(f"Issues found: {len(result.issues)}")
    for issue in result.issues:
        print(f"  Line {issue.line}: [{issue.severity}] {issue.message}")
    print(f"Metrics: {result.metrics}")
    
    # Example 3: Syntax error
    print("\n" + "=" * 60)
    print("Example 3: Analyzing code with syntax error")
    print("=" * 60)
    syntax_error_code = '''
def broken_function(
    print("missing closing parenthesis")
'''
    result = analyzer.analyze(syntax_error_code)
    print(f"Status: {result.status}")
    print(f"Issues found: {len(result.issues)}")
    for issue in result.issues:
        print(f"  Line {issue.line}: [{issue.severity}] {issue.message}")


if __name__ == "__main__":
    main()

# Made with Bob
