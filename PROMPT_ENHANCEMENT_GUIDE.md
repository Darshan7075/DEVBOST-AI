# Prompt Enhancement Guide

## Overview
The `enhance_prompt` function provides flexible prompt enhancement capabilities with multiple levels of detail and structure.

## Function Signature
```python
def enhance_prompt(prompt: str, level: str = "basic") -> str:
    """
    Enhance a prompt with additional formatting and structure
    
    Args:
        prompt: Base prompt to enhance
        level: Enhancement level ('basic', 'advanced', or 'detailed')
        
    Returns:
        str: Enhanced prompt with additional instructions
    """
```

## Enhancement Levels

### 1. Basic (Default)
Returns the prompt unchanged. Use when you want minimal, straightforward output.

**Example:**
```python
prompt = "Analyze this code repository"
enhanced = enhance_prompt(prompt, "basic")
# Output: "Analyze this code repository"
```

### 2. Advanced
Adds developer-friendly structured output instructions with:
- Structured output formatting
- Bullet points for clarity
- Developer-friendly language
- Code examples where applicable
- Priority levels for critical issues
- Best practices and alternatives

**Example:**
```python
prompt = "Identify bugs in the repository"
enhanced = enhance_prompt(prompt, "advanced")
# Output includes additional instructions for structured, developer-friendly output
```

**Use Cases:**
- Bug analysis with prioritization
- Code reviews requiring actionable feedback
- Security audits with severity levels
- Performance optimization suggestions

### 3. Detailed
Adds comprehensive explanation instructions with:
- In-depth explanations
- Relevant documentation links
- Context and reasoning behind suggestions

**Example:**
```python
prompt = "Generate documentation for this project"
enhanced = enhance_prompt(prompt, "detailed")
# Output includes instructions for comprehensive documentation with links
```

**Use Cases:**
- Documentation generation
- Educational content creation
- Architectural explanations
- Onboarding materials

## Integration with get_prompt

The `get_prompt` function now supports enhancement levels:

```python
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
```

### Usage Examples

#### Basic Bug Analysis
```python
from src.utils.prompt_generator import get_prompt

prompt = get_prompt("bugs", "https://github.com/user/repo", "basic")
# Returns standard bug analysis prompt
```

#### Advanced Bug Analysis with Prioritization
```python
prompt = get_prompt("bugs", "https://github.com/user/repo", "advanced")
# Returns bug analysis prompt with structured output and priority levels
```

#### Detailed Documentation Generation
```python
prompt = get_prompt("docs", "https://github.com/user/repo", "detailed")
# Returns documentation prompt with comprehensive explanation requirements
```

## Best Practices

1. **Choose the Right Level:**
   - Use `basic` for quick, straightforward analysis
   - Use `advanced` for actionable, prioritized feedback
   - Use `detailed` for comprehensive, educational content

2. **Task-Level Matching:**
   - `bugs` + `advanced` = Prioritized bug reports with fixes
   - `docs` + `detailed` = Comprehensive documentation with context
   - `tests` + `advanced` = Structured test cases with examples
   - `explain` + `detailed` = In-depth architectural explanations

3. **Performance Considerations:**
   - More detailed prompts may result in longer response times
   - Advanced/detailed levels generate more comprehensive outputs
   - Consider your use case and time constraints

## Testing

Run the test suite to verify functionality:

```bash
python test_prompt_enhancement.py
```

This will demonstrate all three enhancement levels with different task types.

## API Integration

When using the API, specify the enhancement level in your request:

```python
import requests

response = requests.post("http://localhost:8000/analyze", json={
    "repo_url": "https://github.com/user/repo",
    "task": "bugs",
    "enhancement_level": "advanced"  # Optional, defaults to "basic"
})
```

## Future Enhancements

Potential improvements for future versions:
- Custom enhancement templates
- Language-specific enhancements
- Framework-specific instructions
- Team-specific coding standards integration
- AI model-specific optimizations

## Contributing

When adding new enhancement levels:
1. Add the level to the `enhance_prompt` function
2. Update this documentation
3. Add test cases to `test_prompt_enhancement.py`
4. Update API documentation if applicable

---

**Last Updated:** 2026-05-01  
**Version:** 1.0.0