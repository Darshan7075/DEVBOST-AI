"""
DevBoost AI - Demo Script
Run this to see the code analyzer in action without interactive input
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from core.code_analyzer import CodeAnalyzer


def print_banner():
    """Print application banner"""
    print("\n" + "=" * 70)
    print("          DevBoost AI v1.0.0 - Code Analyzer Demo")
    print("=" * 70 + "\n")


def main():
    """Run demo"""
    print_banner()
    
    analyzer = CodeAnalyzer()
    
    # Example 1: Clean code
    print("Example 1: Analyzing clean, well-written code")
    print("-" * 70)
    clean_code = '''
def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers: List of numeric values
        
    Returns:
        float: The average value
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
'''
    
    print("Code:")
    print(clean_code)
    
    result = analyzer.analyze(clean_code, "python")
    print(f"\n[OK] Analysis Status: {result.status.upper()}")
    print(f"[*] Metrics:")
    print(f"   - Lines of Code: {result.metrics.lines_of_code}")
    print(f"   - Functions: {result.metrics.functions}")
    print(f"   - Complexity: {result.metrics.complexity}")
    print(f"   - Maintainability Score: {result.metrics.maintainability}/100")
    print(f"[*] Issues Found: {len(result.issues)}")
    
    if result.issues:
        for issue in result.issues:
            print(f"   Line {issue.line}: [{issue.severity.upper()}] {issue.message}")
    
    # Example 2: Code with issues
    print("\n\n" + "=" * 70)
    print("Example 2: Analyzing code with multiple issues")
    print("-" * 70)
    problematic_code = '''
def complex_function(x, y, z):
    if x > 0:
        if y > 0:
            if z > 0:
                if x > 10:
                    if y > 10:
                        return "very complex"
                    else:
                        return "complex"
                else:
                    return "medium"
            else:
                return "low"
        else:
            return "negative y"
    else:
        return "negative x"

password = "admin123"

def unsafe_query(user_input):
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    return query

def dangerous_eval(code):
    return eval(code)
'''
    
    print("Code:")
    print(problematic_code)
    
    result = analyzer.analyze(problematic_code, "python")
    print(f"\n[WARN] Analysis Status: {result.status.upper()}")
    print(f"[*] Metrics:")
    print(f"   - Lines of Code: {result.metrics.lines_of_code}")
    print(f"   - Functions: {result.metrics.functions}")
    print(f"   - Complexity: {result.metrics.complexity}")
    print(f"   - Maintainability Score: {result.metrics.maintainability}/100")
    print(f"\n[*] Issues Found: {len(result.issues)}")
    
    if result.issues:
        for issue in result.issues:
            severity_icon = {
                'error': '[ERROR]',
                'warning': '[WARN]',
                'info': '[INFO]'
            }.get(issue.severity, '[*]')
            print(f"\n   {severity_icon} Line {issue.line}: {issue.category}")
            print(f"      Message: {issue.message}")
            if issue.suggestion:
                print(f"      [TIP] {issue.suggestion}")
    
    # Example 3: Syntax error
    print("\n\n" + "=" * 70)
    print("Example 3: Analyzing code with syntax error")
    print("-" * 70)
    syntax_error_code = '''
def broken_function(x, y
    print("Missing closing parenthesis")
    return x + y
'''
    
    print("Code:")
    print(syntax_error_code)
    
    result = analyzer.analyze(syntax_error_code, "python")
    print(f"\n[ERROR] Analysis Status: {result.status.upper()}")
    print(f"[*] Issues Found: {len(result.issues)}")
    
    if result.issues:
        for issue in result.issues:
            print(f"\n   [ERROR] Line {issue.line}: {issue.category}")
            print(f"      Message: {issue.message}")
            if issue.suggestion:
                print(f"      [TIP] {issue.suggestion}")
    
    print("\n" + "=" * 70)
    print("Demo Complete!")
    print("=" * 70)
    print("\nTo run the full interactive application, use: python src/main.py")
    print("Visit: https://github.com/Darshan7075/DEVBOST-AI\n")


if __name__ == "__main__":
    main()

# Made with Bob
