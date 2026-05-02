"""
Test script for enhanced prompt generator
Demonstrates the enhance_prompt function with different levels
"""

from src.utils.prompt_generator import get_prompt, enhance_prompt

def test_enhance_prompt():
    """Test the enhance_prompt function with different levels"""
    
    print("=" * 80)
    print("PROMPT ENHANCEMENT TEST")
    print("=" * 80)
    
    base_prompt = "Analyze this code repository for bugs and security issues."
    
    # Test basic level
    print("\n1. BASIC LEVEL (default)")
    print("-" * 80)
    basic = enhance_prompt(base_prompt, "basic")
    print(basic)
    
    # Test advanced level
    print("\n2. ADVANCED LEVEL")
    print("-" * 80)
    advanced = enhance_prompt(base_prompt, "advanced")
    print(advanced)
    
    # Test detailed level
    print("\n3. DETAILED LEVEL")
    print("-" * 80)
    detailed = enhance_prompt(base_prompt, "detailed")
    print(detailed)


def test_integrated_prompts():
    """Test the integrated get_prompt function with enhancement levels"""
    
    print("\n" + "=" * 80)
    print("INTEGRATED PROMPT GENERATION TEST")
    print("=" * 80)
    
    repo_url = "https://github.com/example/repo"
    
    # Test with basic enhancement
    print("\n1. BUGS ANALYSIS - BASIC")
    print("-" * 80)
    basic_bugs = get_prompt("bugs", repo_url, "basic")
    print(basic_bugs)
    
    # Test with advanced enhancement
    print("\n2. BUGS ANALYSIS - ADVANCED")
    print("-" * 80)
    advanced_bugs = get_prompt("bugs", repo_url, "advanced")
    print(advanced_bugs)
    
    # Test with detailed enhancement
    print("\n3. DOCS GENERATION - DETAILED")
    print("-" * 80)
    detailed_docs = get_prompt("docs", repo_url, "detailed")
    print(detailed_docs)


if __name__ == "__main__":
    test_enhance_prompt()
    test_integrated_prompts()
    
    print("\n" + "=" * 80)
    print("[SUCCESS] All tests completed successfully!")
    print("=" * 80)

# Made with Bob
