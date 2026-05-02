"""
Example Usage: Demonstrating enhance_prompt workflow
Shows how to use get_prompt and enhance_prompt separately
"""

from src.utils.prompt_generator import get_prompt, enhance_prompt


def example_basic_workflow():
    """Example: Basic workflow without enhancement"""
    print("=" * 80)
    print("EXAMPLE 1: Basic Workflow (No Enhancement)")
    print("=" * 80)
    
    task = "bugs"
    repo = "https://github.com/example/my-project"
    
    # Get basic prompt
    prompt = get_prompt(task, repo)
    print(prompt)


def example_advanced_workflow():
    """Example: Advanced workflow with enhancement"""
    print("\n" + "=" * 80)
    print("EXAMPLE 2: Advanced Workflow (With Enhancement)")
    print("=" * 80)
    
    task = "bugs"
    repo = "https://github.com/example/my-project"
    
    # Get prompt and then enhance it
    prompt = get_prompt(task, repo)
    prompt = enhance_prompt(prompt, level="advanced")
    print(prompt)


def example_detailed_workflow():
    """Example: Detailed workflow for documentation"""
    print("\n" + "=" * 80)
    print("EXAMPLE 3: Detailed Workflow (Documentation)")
    print("=" * 80)
    
    task = "docs"
    repo = "https://github.com/example/my-project"
    
    # Get prompt and enhance with detailed level
    prompt = get_prompt(task, repo)
    prompt = enhance_prompt(prompt, level="detailed")
    print(prompt)


def example_conditional_enhancement():
    """Example: Conditional enhancement based on user preference"""
    print("\n" + "=" * 80)
    print("EXAMPLE 4: Conditional Enhancement")
    print("=" * 80)
    
    task = "tests"
    repo = "https://github.com/example/my-project"
    user_wants_detailed = True  # This could come from user input or config
    
    # Get base prompt
    prompt = get_prompt(task, repo)
    
    # Conditionally enhance based on user preference
    if user_wants_detailed:
        prompt = enhance_prompt(prompt, level="advanced")
        print("Enhanced with advanced level:")
    else:
        print("Basic prompt (no enhancement):")
    
    print(prompt)


def example_multiple_tasks():
    """Example: Processing multiple tasks with different enhancement levels"""
    print("\n" + "=" * 80)
    print("EXAMPLE 5: Multiple Tasks with Different Enhancements")
    print("=" * 80)
    
    repo = "https://github.com/example/my-project"
    
    # Define tasks with their preferred enhancement levels
    tasks_config = [
        ("explain", "basic"),
        ("bugs", "advanced"),
        ("docs", "detailed"),
        ("tests", "advanced")
    ]
    
    for task, level in tasks_config:
        print(f"\n--- Task: {task.upper()} (Enhancement: {level}) ---")
        prompt = get_prompt(task, repo)
        prompt = enhance_prompt(prompt, level=level)
        print(prompt[:200] + "..." if len(prompt) > 200 else prompt)


def example_custom_enhancement_pipeline():
    """Example: Custom enhancement pipeline"""
    print("\n" + "=" * 80)
    print("EXAMPLE 6: Custom Enhancement Pipeline")
    print("=" * 80)
    
    task = "bugs"
    repo = "https://github.com/example/my-project"
    
    # Step 1: Get base prompt
    prompt = get_prompt(task, repo)
    print("Step 1 - Base Prompt:")
    print(prompt)
    
    # Step 2: Apply advanced enhancement
    prompt = enhance_prompt(prompt, level="advanced")
    print("\nStep 2 - After Advanced Enhancement:")
    print(prompt)
    
    # Step 3: Add custom instructions (you can further customize)
    custom_addition = """

ADDITIONAL REQUIREMENTS:
- Focus on security vulnerabilities first
- Provide OWASP Top 10 references where applicable
- Include remediation timeline estimates
"""
    prompt = prompt + custom_addition
    print("\nStep 3 - After Custom Addition:")
    print(prompt)


if __name__ == "__main__":
    # Run all examples
    example_basic_workflow()
    example_advanced_workflow()
    example_detailed_workflow()
    example_conditional_enhancement()
    example_multiple_tasks()
    example_custom_enhancement_pipeline()
    
    print("\n" + "=" * 80)
    print("[SUCCESS] All examples completed!")
    print("=" * 80)
    print("\nKey Takeaway:")
    print("Use this pattern for flexible prompt enhancement:")
    print("  prompt = get_prompt(task, repo)")
    print("  prompt = enhance_prompt(prompt, level='advanced')")
    print("=" * 80)

# Made with Bob
