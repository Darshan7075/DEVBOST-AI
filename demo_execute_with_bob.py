"""
Demo: Complete Workflow with execute_with_bob
Shows end-to-end usage of the enhanced prompt system
"""

from src.utils.prompt_generator import execute_with_bob
import json


def print_response(response, title):
    """Pretty print the response"""
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)
    print(f"Status: {response['status']}")
    print(f"Task: {response['task']}")
    print(f"Repository: {response['repo']}")
    print(f"Enhancement Level: {response['enhancement_level']}")
    print(f"\nPrompt Length: {response['metadata']['prompt_length']} characters")
    print(f"\n--- Prompt Used ---")
    print(response['prompt_used'])
    print(f"\n--- Output ---")
    print(response['output'])


def demo_basic_usage():
    """Demo 1: Basic usage without enhancement"""
    print("\n" + "#" * 80)
    print("# DEMO 1: Basic Usage (No Enhancement)")
    print("#" * 80)
    
    repo_url = "https://github.com/example/my-project"
    
    # Execute with basic level (default)
    response = execute_with_bob(repo_url, "explain", level="basic")
    print_response(response, "Project Explanation - Basic")


def demo_advanced_bug_analysis():
    """Demo 2: Advanced bug analysis"""
    print("\n" + "#" * 80)
    print("# DEMO 2: Advanced Bug Analysis")
    print("#" * 80)
    
    repo_url = "https://github.com/example/security-app"
    
    # Execute with advanced level for structured output
    response = execute_with_bob(repo_url, "bugs", level="advanced")
    print_response(response, "Bug Analysis - Advanced")


def demo_detailed_documentation():
    """Demo 3: Detailed documentation generation"""
    print("\n" + "#" * 80)
    print("# DEMO 3: Detailed Documentation Generation")
    print("#" * 80)
    
    repo_url = "https://github.com/example/api-service"
    
    # Execute with detailed level for comprehensive docs
    response = execute_with_bob(repo_url, "docs", level="detailed")
    print_response(response, "Documentation Generation - Detailed")


def demo_multiple_tasks():
    """Demo 4: Process multiple tasks with different levels"""
    print("\n" + "#" * 80)
    print("# DEMO 4: Multiple Tasks with Different Enhancement Levels")
    print("#" * 80)
    
    repo_url = "https://github.com/example/full-stack-app"
    
    tasks = [
        ("explain", "basic", "Quick project overview"),
        ("bugs", "advanced", "Prioritized bug report"),
        ("tests", "advanced", "Structured test cases"),
        ("docs", "detailed", "Comprehensive documentation")
    ]
    
    results = []
    for task, level, description in tasks:
        print(f"\n--- Processing: {description} ---")
        response = execute_with_bob(repo_url, task, level=level)
        results.append(response)
        print(f"[OK] {task.upper()} completed with {level} enhancement")
        print(f"  Prompt length: {response['metadata']['prompt_length']} chars")
    
    print("\n" + "=" * 80)
    print("Summary of All Tasks")
    print("=" * 80)
    for i, (task, level, desc) in enumerate(tasks, 1):
        print(f"{i}. {desc}")
        print(f"   Task: {task}, Level: {level}")
        print(f"   Status: {results[i-1]['status']}")


def demo_comparison():
    """Demo 5: Compare different enhancement levels for same task"""
    print("\n" + "#" * 80)
    print("# DEMO 5: Enhancement Level Comparison")
    print("#" * 80)
    
    repo_url = "https://github.com/example/comparison-test"
    task = "bugs"
    
    levels = ["basic", "advanced", "detailed"]
    
    print(f"\nAnalyzing same repository with different enhancement levels:")
    print(f"Repository: {repo_url}")
    print(f"Task: {task}")
    
    for level in levels:
        response = execute_with_bob(repo_url, task, level=level)
        print(f"\n{'=' * 80}")
        print(f"Enhancement Level: {level.upper()}")
        print(f"{'=' * 80}")
        print(f"Prompt Length: {response['metadata']['prompt_length']} characters")
        print(f"\nPrompt Preview (first 300 chars):")
        print(response['prompt_used'][:300] + "...")


def demo_json_export():
    """Demo 6: Export response as JSON"""
    print("\n" + "#" * 80)
    print("# DEMO 6: JSON Export for API Integration")
    print("#" * 80)
    
    repo_url = "https://github.com/example/api-integration"
    
    # Execute and get response
    response = execute_with_bob(repo_url, "bugs", level="advanced")
    
    # Convert to JSON
    json_output = json.dumps(response, indent=2)
    
    print("\nJSON Response (for API integration):")
    print(json_output)
    
    print("\n--- Usage in API ---")
    print("This JSON can be:")
    print("1. Returned from REST API endpoints")
    print("2. Stored in databases")
    print("3. Sent to message queues")
    print("4. Used in webhooks")


def main():
    """Run all demos"""
    print("=" * 80)
    print("EXECUTE WITH BOB - COMPLETE WORKFLOW DEMONSTRATION")
    print("=" * 80)
    print("\nThis demo shows the complete end-to-end workflow:")
    print("1. Get base prompt")
    print("2. Enhance with chosen level")
    print("3. Execute with IBM Bob (simulated)")
    print("4. Return structured response")
    
    # Run all demos
    demo_basic_usage()
    demo_advanced_bug_analysis()
    demo_detailed_documentation()
    demo_multiple_tasks()
    demo_comparison()
    demo_json_export()
    
    # Final summary
    print("\n" + "=" * 80)
    print("DEMO COMPLETE!")
    print("=" * 80)
    print("\nKey Takeaways:")
    print("[OK] Simple API: execute_with_bob(repo_url, task, level)")
    print("[OK] Three enhancement levels: basic, advanced, detailed")
    print("[OK] Structured JSON response")
    print("[OK] Ready for production integration")
    print("\nNext Steps:")
    print("1. Replace mock with actual IBM watsonx API call")
    print("2. Add error handling and retries")
    print("3. Implement caching for repeated requests")
    print("4. Add rate limiting and quota management")
    print("=" * 80)


if __name__ == "__main__":
    main()

# Made with Bob
