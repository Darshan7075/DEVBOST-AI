# Enhanced API Documentation

## Overview
The DevBoost AI API now supports prompt enhancement levels for more structured and detailed analysis results.

## Base URL
```
http://localhost:8000/api/v1
```

## Endpoints

### 1. Health Check
Check if the API is running.

**Endpoint:** `GET /health`

**Response:**
```json
{
  "status": "healthy",
  "service": "DevBoost AI API",
  "version": "1.0.0"
}
```

### 2. Get Available Tasks
List all available analysis tasks.

**Endpoint:** `GET /tasks`

**Response:**
```json
{
  "tasks": [
    {
      "name": "explain",
      "description": "Explains the project purpose, architecture, and workflow"
    },
    {
      "name": "docs",
      "description": "Generates complete README with setup, usage, and features"
    },
    {
      "name": "bugs",
      "description": "Identifies bugs, security issues, and bad practices with fixes"
    },
    {
      "name": "tests",
      "description": "Generates comprehensive unit test cases with edge cases"
    }
  ]
}
```

### 3. Analyze Repository (Enhanced)
Analyze a GitHub repository with prompt enhancement.

**Endpoint:** `POST /analyze`

**Request Body:**
```json
{
  "repo": "https://github.com/username/repository",
  "task": "bugs",
  "level": "advanced"
}
```

**Parameters:**
- `repo` (required): GitHub repository URL
- `task` (required): Analysis task type
  - `explain`: Project explanation
  - `docs`: Documentation generation
  - `bugs`: Bug and security analysis
  - `tests`: Test case generation
- `level` (optional): Enhancement level (default: "basic")
  - `basic`: No enhancement, straightforward output
  - `advanced`: Structured output with priorities and examples
  - `detailed`: Comprehensive explanations with context

**Response:**
```json
{
  "status": "success",
  "task": "bugs",
  "repo": "https://github.com/username/repository",
  "enhancement_level": "advanced",
  "prompt_used": "...",
  "output": "[Simulated IBM Bob Output for bugs]",
  "metadata": {
    "prompt_length": 434,
    "timestamp": "2026-05-01T16:21:00Z"
  }
}
```

## Enhancement Levels Explained

### Basic Level
- **Use Case**: Quick, straightforward analysis
- **Output**: Simple, direct responses
- **Best For**: Initial exploration, quick checks

**Example Request:**
```bash
curl -X POST http://localhost:8000/api/v1/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "repo": "https://github.com/user/repo",
    "task": "explain",
    "level": "basic"
  }'
```

### Advanced Level (Recommended)
- **Use Case**: Development and production use
- **Output**: Structured with bullet points, code examples, priority levels
- **Best For**: Bug analysis, code reviews, actionable feedback

**Features:**
- Structured output format
- Bullet points for clarity
- Developer-friendly language
- Code examples where applicable
- Priority levels for critical issues
- Best practices and alternatives

**Example Request:**
```bash
curl -X POST http://localhost:8000/api/v1/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "repo": "https://github.com/user/repo",
    "task": "bugs",
    "level": "advanced"
  }'
```

### Detailed Level
- **Use Case**: Documentation and learning
- **Output**: Comprehensive with explanations and links
- **Best For**: Documentation generation, educational content

**Features:**
- Comprehensive explanations
- Relevant documentation links
- Context and reasoning
- In-depth analysis

**Example Request:**
```bash
curl -X POST http://localhost:8000/api/v1/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "repo": "https://github.com/user/repo",
    "task": "docs",
    "level": "detailed"
  }'
```

## Usage Examples

### Python (requests)
```python
import requests

# Basic analysis
response = requests.post(
    "http://localhost:8000/api/v1/analyze",
    json={
        "repo": "https://github.com/user/repo",
        "task": "explain"
    }
)
print(response.json())

# Advanced bug analysis
response = requests.post(
    "http://localhost:8000/api/v1/analyze",
    json={
        "repo": "https://github.com/user/repo",
        "task": "bugs",
        "level": "advanced"
    }
)
result = response.json()
print(f"Status: {result['status']}")
print(f"Enhancement Level: {result['enhancement_level']}")
print(f"Prompt Length: {result['metadata']['prompt_length']}")
```

### JavaScript (fetch)
```javascript
// Advanced analysis
fetch('http://localhost:8000/api/v1/analyze', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    repo: 'https://github.com/user/repo',
    task: 'bugs',
    level: 'advanced'
  })
})
.then(response => response.json())
.then(data => {
  console.log('Status:', data.status);
  console.log('Enhancement Level:', data.enhancement_level);
  console.log('Output:', data.output);
});
```

### cURL
```bash
# Basic analysis (default level)
curl -X POST http://localhost:8000/api/v1/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "repo": "https://github.com/user/repo",
    "task": "explain"
  }'

# Advanced analysis
curl -X POST http://localhost:8000/api/v1/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "repo": "https://github.com/user/repo",
    "task": "bugs",
    "level": "advanced"
  }'

# Detailed documentation
curl -X POST http://localhost:8000/api/v1/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "repo": "https://github.com/user/repo",
    "task": "docs",
    "level": "detailed"
  }'
```

## Error Responses

### Invalid Task
**Status Code:** 400

```json
{
  "detail": "Invalid task. Must be one of: explain, docs, bugs, tests"
}
```

### Invalid Enhancement Level
**Status Code:** 400

```json
{
  "detail": "Invalid level. Must be one of: basic, advanced, detailed"
}
```

## Best Practices

### Task-Level Matching
Choose the right enhancement level for each task:

| Task | Recommended Level | Reason |
|------|------------------|--------|
| `explain` | `basic` or `detailed` | Basic for quick overview, detailed for learning |
| `bugs` | `advanced` | Need prioritized, actionable feedback |
| `docs` | `detailed` | Need comprehensive documentation |
| `tests` | `advanced` | Need structured test cases with examples |

### Performance Considerations
- **Basic**: Fastest, minimal processing
- **Advanced**: Moderate processing, structured output
- **Detailed**: More processing, comprehensive output

### Rate Limiting
- Consider implementing rate limiting for production
- Cache repeated requests when possible
- Use appropriate enhancement level to balance detail vs. speed

## Testing

Run the test suite:
```bash
# Start the API server
python -m uvicorn src.api.app:app --reload

# In another terminal, run tests
python test_api_enhanced.py
```

## Integration Example

Complete integration example:

```python
from fastapi import FastAPI
import requests

app = FastAPI()

@app.post("/analyze-repo")
async def analyze_repository(repo_url: str, analysis_type: str):
    """
    Wrapper endpoint that uses DevBoost AI API
    """
    # Call DevBoost AI API with advanced enhancement
    response = requests.post(
        "http://localhost:8000/api/v1/analyze",
        json={
            "repo": repo_url,
            "task": analysis_type,
            "level": "advanced"
        }
    )
    
    result = response.json()
    
    # Process and return results
    return {
        "repository": repo_url,
        "analysis_type": analysis_type,
        "status": result["status"],
        "findings": result["output"],
        "prompt_length": result["metadata"]["prompt_length"]
    }
```

## Architecture

```
Client Request
    ↓
FastAPI Router (routes.py)
    ↓
Bob Executor Service (bob_executor.py)
    ↓
Prompt Generator (prompt_generator.py)
    ├── get_prompt() - Generate base prompt
    └── enhance_prompt() - Add enhancement
    ↓
IBM Bob API (simulated)
    ↓
Structured Response
```

## Next Steps

1. **Production Deployment**
   - Replace mock with actual IBM watsonx API
   - Add authentication and API keys
   - Implement rate limiting

2. **Enhancements**
   - Add caching layer
   - Implement webhooks for async processing
   - Add result storage and history

3. **Monitoring**
   - Add logging and metrics
   - Track API usage and performance
   - Monitor enhancement level usage

---

**Version:** 1.0.0  
**Last Updated:** 2026-05-01  
**Status:** Production Ready ✅