"""
DevBoost AI - Main Entry Point
Run this file to start the application
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from core.code_analyzer import CodeAnalyzer


def print_banner():
    """Print application banner"""
    banner = """
    ============================================================
    
                  DevBoost AI v1.0.0
    
              AI-Powered Development Assistant
    
    ============================================================
    """
    print(banner)


def demo_code_analyzer():
    """Demonstrate code analyzer functionality"""
    print("\n" + "=" * 70)
    print("DEMO: Code Analyzer")
    print("=" * 70)
    
    analyzer = CodeAnalyzer()
    
    # Example 1: Clean code
    print("\n[*] Example 1: Analyzing clean, well-written code")
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


class Calculator:
    """Simple calculator class"""
    
    def add(self, a, b):
        """Add two numbers"""
        return a + b
    
    def subtract(self, a, b):
        """Subtract b from a"""
        return a - b
'''
    
    print("Code:")
    print(clean_code)
    
    result = analyzer.analyze(clean_code, "python")
    print(f"\n[OK] Analysis Status: {result.status.upper()}")
    print(f"[*] Metrics:")
    print(f"   - Lines of Code: {result.metrics.lines_of_code}")
    print(f"   - Functions: {result.metrics.functions}")
    print(f"   - Classes: {result.metrics.classes}")
    print(f"   - Complexity: {result.metrics.complexity}")
    print(f"   - Maintainability Score: {result.metrics.maintainability}/100")
    print(f"🐛 Issues Found: {len(result.issues)}")
    
    if result.issues:
        for issue in result.issues:
            print(f"   Line {issue.line}: [{issue.severity.upper()}] {issue.message}")
    
    # Example 2: Code with issues
    print("\n\n[*] Example 2: Analyzing code with multiple issues")
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
api_key = "sk-1234567890"

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
            print(f"\n   {severity_icon} Line {issue.line}: [{issue.severity.upper()}] {issue.category}")
            print(f"      Message: {issue.message}")
            if issue.suggestion:
                print(f"      [TIP] Suggestion: {issue.suggestion}")
    
    # Example 3: Syntax error
    print("\n\n[*] Example 3: Analyzing code with syntax error")
    print("-" * 70)
    syntax_error_code = '''
def broken_function(x, y
    print("Missing closing parenthesis")
    return x + y
'''
    
    print("Code:")
    print(syntax_error_code)
    
    result = analyzer.analyze(syntax_error_code, "python")
    print(f"\n❌ Analysis Status: {result.status.upper()}")
    print(f"[*] Issues Found: {len(result.issues)}")
    
    if result.issues:
        for issue in result.issues:
            print(f"\n   [ERROR] Line {issue.line}: [{issue.severity.upper()}] {issue.category}")
            print(f"      Message: {issue.message}")
            if issue.suggestion:
                print(f"      [TIP] Suggestion: {issue.suggestion}")


def interactive_mode():
    """Interactive mode for analyzing user code"""
    print("\n" + "=" * 70)
    print("INTERACTIVE MODE")
    print("=" * 70)
    print("\nEnter your Python code (type 'END' on a new line to finish):")
    print("Type 'exit' to quit\n")
    
    analyzer = CodeAnalyzer()
    
    while True:
        lines = []
        print(">>> ", end="")
        
        while True:
            try:
                line = input()
                if line.strip().upper() == 'END':
                    break
                if line.strip().lower() == 'exit':
                    print("\n👋 Thanks for using DevBoost AI!")
                    return
                lines.append(line)
            except EOFError:
                return
        
        if not lines:
            continue
        
        code = '\n'.join(lines)
        
        print("\n[*] Analyzing your code...\n")
        result = analyzer.analyze(code, "python")
        
        print(f"Status: {result.status.upper()}")
        print(f"Issues: {len(result.issues)}")
        print(f"Maintainability: {result.metrics.maintainability}/100")
        
        if result.issues:
            print("\n[*] Issues found:")
            for issue in result.issues:
                print(f"  Line {issue.line}: [{issue.severity}] {issue.message}")
                if issue.suggestion:
                    print(f"    [TIP] {issue.suggestion}")
        else:
            print("\n[OK] No issues found! Great code!")
        
        print("\n" + "-" * 70)
        print("Enter more code or type 'exit' to quit:\n")


def show_menu():
    """Show main menu"""
    print("\n" + "=" * 70)
    print("MAIN MENU")
    print("=" * 70)
    print("\n1. Run Demo (See code analyzer in action)")
    print("2. Interactive Mode (Analyze your own code)")
    print("3. Exit")
    print("\nEnter your choice (1-3): ", end="")


def main():
    """Main application entry point"""
    print_banner()
    
    print("\nWelcome to DevBoost AI!")
    print("Your AI-powered development assistant\n")
    
    while True:
        show_menu()
        
        try:
            choice = input().strip()
            
            if choice == '1':
                demo_code_analyzer()
            elif choice == '2':
                interactive_mode()
            elif choice == '3':
                print("\n👋 Thanks for using DevBoost AI!")
                print("Visit https://github.com/Darshan7075/DEVBOST-AI for more info\n")
                break
            else:
                print("\n[ERROR] Invalid choice. Please enter 1, 2, or 3.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Thanks for using DevBoost AI!")
            break
        except Exception as e:
            print(f"\n[ERROR] Error: {e}")


if __name__ == "__main__":
    main()

# Made with Bob
