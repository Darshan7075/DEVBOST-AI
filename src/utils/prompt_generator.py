"""
Prompt Generator for Repository Analysis
Generates structured prompts for different analysis tasks
"""


def get_prompt(task: str, repo_url: str, enhancement_level: str = "basic") -> str:
    """
    Generate analysis prompt based on task type
    
    Args:
        task: Type of analysis ('explain', 'docs', 'bugs', 'tests')
        repo_url: GitHub repository URL
        enhancement_level: Level of prompt enhancement ('basic', 'advanced', 'detailed')
        
    Returns:
        str: Formatted prompt for the analysis task
    """
    base = f"""
Using IBM Bob's full repository context understanding,
analyze the following repository:

{repo_url}

"""

    prompts = {
        "explain": base + """
Explain the project in simple terms.
Include:
- Purpose
- Architecture
- Workflow
""",

        "docs": base + """
Generate a complete README.md including:
- Description
- Setup
- Usage
- Features
""",

        "bugs": base + """
Identify:
- Bugs
- Security issues
- Bad practices

Suggest fixes with examples.
""",

        "tests": base + """
Generate unit test cases:
- Inputs
- Expected outputs
- Edge cases
"""
    }

    base_prompt = prompts.get(task, base + "Explain this project.")
    return enhance_prompt(base_prompt, enhancement_level)


def get_all_tasks() -> list:
    """
    Get list of available analysis tasks
    
    Returns:
        list: Available task types
    """
    return ["explain", "docs", "bugs", "tests"]


def get_task_description(task: str) -> str:
    """
    Get description of what each task does
    
    Args:
        task: Task type
        
    Returns:
        str: Description of the task
    """
    descriptions = {
        "explain": "Explains the project purpose, architecture, and workflow",
        "docs": "Generates complete README with setup, usage, and features",
        "bugs": "Identifies bugs, security issues, and bad practices with fixes",
        "tests": "Generates comprehensive unit test cases with edge cases"
    }
    return descriptions.get(task, "Unknown task")


def enhance_prompt(prompt: str, level: str = "basic") -> str:
    """
    Enhance a prompt with additional formatting and structure
    
    Args:
        prompt: Base prompt to enhance
        level: Enhancement level ('basic' or 'advanced')
        
    Returns:
        str: Enhanced prompt with additional instructions
    """
    if level == "advanced":
        return prompt + """

Also:
- Provide structured output
- Use bullet points
- Keep it developer-friendly
- Include code examples where applicable
- Highlight critical issues with priority levels
- Suggest best practices and alternatives
"""
    elif level == "detailed":
        return prompt + """

Additionally:
- Provide comprehensive explanations
- Include relevant documentation links
- Add context and reasoning
"""
    return prompt


def execute_with_bob(repo_url: str, task: str, level: str = "basic"):
    """
    Execute analysis with IBM Bob using enhanced prompts
    
    Args:
        repo_url: GitHub repository URL
        task: Type of analysis ('explain', 'docs', 'bugs', 'tests')
        level: Enhancement level ('basic', 'advanced', 'detailed')
        
    Returns:
        dict: Response containing status, task info, and output
    """
    # Step 1: Get base prompt
    prompt = get_prompt(task, repo_url)
    
    # Step 2: Enhance the prompt
    prompt = enhance_prompt(prompt, level)
    
    # Step 3: Send to IBM Bob (mock for now)
    # In production, this would call the actual IBM watsonx API
    response = {
        "status": "success",
        "task": task,
        "repo": repo_url,
        "enhancement_level": level,
        "prompt_used": prompt,
        "output": f"[Simulated IBM Bob Output for {task}]",
        "metadata": {
            "prompt_length": len(prompt),
            "timestamp": "2026-05-01T16:18:00Z"
        }
    }
    
    return response


def demo():
    """Demo the prompt generator"""
    print("=" * 70)
    print("Prompt Generator Demo")
    print("=" * 70)
    
    repo_url = "https://github.com/Darshan7075/DEVBOST-AI"
    
    print(f"\nRepository: {repo_url}\n")
    
    for task in get_all_tasks():
        print(f"\n{'=' * 70}")
        print(f"Task: {task.upper()}")
        print(f"Description: {get_task_description(task)}")
        print(f"{'=' * 70}")
        print("\nGenerated Prompt:")
        print("-" * 70)
        print(get_prompt(task, repo_url))


if __name__ == "__main__":
    demo()

# Made with Bob
