# 🌐 DevBoost AI - API Documentation

**Version:** 1.0.0  
**Base URL:** `http://localhost:8000`  
**API Prefix:** `/api/v1`

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Getting Started](#getting-started)
3. [Authentication](#authentication)
4. [Endpoints](#endpoints)
5. [Request/Response Examples](#requestresponse-examples)
6. [Error Handling](#error-handling)
7. [Rate Limiting](#rate-limiting)
8. [Integration Guide](#integration-guide)

---

## 🎯 Overview

The DevBoost AI API provides programmatic access to repository analysis capabilities. It uses the prompt generator utility to create structured analysis requests that can be sent to IBM Bob or other AI services.

### Key Features:
- ✅ Repository analysis with multiple task types
- ✅ RESTful API design
- ✅ JSON request/response format
- ✅ Interactive API documentation (Swagger UI)
- ✅ Automatic request validation
- ✅ CORS support for web applications

---

## 🚀 Getting Started

### Installation

1. **Install Dependencies:**
```bash
pip install fastapi uvicorn pydantic
```

2. **Start the Server:**
```bash
python src/api/app.py
```

3. **Access API Documentation:**
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- Root: http://localhost:8000

### Quick Test

```bash
# Test the API without starting server
python test_api.py
```

---

## 🔐 Authentication

**Current Status:** No authentication required (development mode)

**Production Recommendations:**
- Implement API key authentication
- Use OAuth 2.0 for user-based access
- Add rate limiting per API key
- Enable HTTPS only

**Example Future Implementation:**
```python
from fastapi import Header, HTTPException

async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != "your-secret-key":
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return x_api_key
```

---

## 📡 Endpoints

### 1. Root Endpoint

**GET** `/`

Get API information and available endpoints.

**Response:**
```json
{
  "service": "DevBoost AI API",
  "version": "1.0.0",
  "description": "AI-Powered Development Assistant",
  "docs": "/docs",
  "endpoints": {
    "analyze": "/api/v1/analyze",
    "tasks": "/api/v1/tasks",
    "health": "/api/v1/health"
  }
}
```

---

### 2. Analyze Repository

**POST** `/api/v1/analyze`

Analyze a GitHub repository with specified task type.

**Request Body:**
```json
{
  "repo": "https://github.com/username/repository",
  "task": "explain"
}
```

**Parameters:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| repo | string | Yes | GitHub repository URL |
| task | string | Yes | Analysis task type (explain, docs, bugs, tests) |

**Response:**
```json
{
  "result": "AI generated analysis output",
  "task": "explain",
  "repo": "https://github.com/username/repository",
  "prompt": "Generated prompt sent to AI"
}
```

**Status Codes:**
- `200 OK` - Successful analysis
- `400 Bad Request` - Invalid task type
- `422 Unprocessable Entity` - Invalid request format
- `500 Internal Server Error` - Server error

---

### 3. Get Available Tasks

**GET** `/api/v1/tasks`

Get list of available analysis task types.

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

---

### 4. Health Check

**GET** `/api/v1/health`

Check API service health status.

**Response:**
```json
{
  "status": "healthy",
  "service": "DevBoost AI API",
  "version": "1.0.0"
}
```

---

## 📝 Request/Response Examples

### Example 1: Explain Project

**Request:**
```bash
curl -X POST "http://localhost:8000/api/v1/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "repo": "https://github.com/Darshan7075/DEVBOST-AI",
    "task": "explain"
  }'
```

**Response:**
```json
{
  "result": "[IBM Bob Response]\n\nRepository: https://github.com/Darshan7075/DEVBOST-AI\nTask: explain\n...",
  "task": "explain",
  "repo": "https://github.com/Darshan7075/DEVBOST-AI",
  "prompt": "Using IBM Bob's full repository context understanding,\nanalyze the following repository:\n\nhttps://github.com/Darshan7075/DEVBOST-AI\n\nExplain the project in simple terms.\nInclude:\n- Purpose\n- Architecture\n- Workflow\n"
}
```

---

### Example 2: Generate Documentation

**Request:**
```bash
curl -X POST "http://localhost:8000/api/v1/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "repo": "https://github.com/username/project",
    "task": "docs"
  }'
```

**Python Example:**
```python
import requests

url = "http://localhost:8000/api/v1/analyze"
data = {
    "repo": "https://github.com/username/project",
    "task": "docs"
}

response = requests.post(url, json=data)
result = response.json()

print(f"Task: {result['task']}")
print(f"Result: {result['result']}")
```

---

### Example 3: Find Bugs

**Request:**
```bash
curl -X POST "http://localhost:8000/api/v1/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "repo": "https://github.com/username/project",
    "task": "bugs"
  }'
```

**JavaScript Example:**
```javascript
const response = await fetch('http://localhost:8000/api/v1/analyze', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    repo: 'https://github.com/username/project',
    task: 'bugs'
  })
});

const data = await response.json();
console.log(data.result);
```

---

### Example 4: Generate Tests

**Request:**
```bash
curl -X POST "http://localhost:8000/api/v1/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "repo": "https://github.com/username/project",
    "task": "tests"
  }'
```

---

## ⚠️ Error Handling

### Error Response Format

```json
{
  "detail": "Error message description"
}
```

### Common Errors

#### 400 Bad Request - Invalid Task
```json
{
  "detail": "Invalid task. Must be one of: explain, docs, bugs, tests"
}
```

**Solution:** Use one of the valid task types.

#### 422 Unprocessable Entity - Validation Error
```json
{
  "detail": [
    {
      "loc": ["body", "repo"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

**Solution:** Ensure all required fields are provided in correct format.

#### 500 Internal Server Error
```json
{
  "error": "Internal server error",
  "detail": "Error description"
}
```

**Solution:** Check server logs for details.

---

## 🚦 Rate Limiting

**Current Status:** No rate limiting (development mode)

**Production Recommendations:**
- Implement rate limiting: 100 requests per minute per IP
- Use Redis for distributed rate limiting
- Return `429 Too Many Requests` when limit exceeded

**Example Implementation:**
```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.post("/api/v1/analyze")
@limiter.limit("100/minute")
async def analyze(request: Request, data: AnalyzeRequest):
    # ... endpoint logic
```

---

## 🔧 Integration Guide

### Python Integration

```python
import requests

class DevBoostClient:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
        self.api_url = f"{base_url}/api/v1"
    
    def analyze(self, repo: str, task: str):
        """Analyze a repository"""
        response = requests.post(
            f"{self.api_url}/analyze",
            json={"repo": repo, "task": task}
        )
        response.raise_for_status()
        return response.json()
    
    def get_tasks(self):
        """Get available tasks"""
        response = requests.get(f"{self.api_url}/tasks")
        return response.json()
    
    def health_check(self):
        """Check API health"""
        response = requests.get(f"{self.api_url}/health")
        return response.json()

# Usage
client = DevBoostClient()
result = client.analyze(
    repo="https://github.com/user/repo",
    task="explain"
)
print(result['result'])
```

---

### JavaScript/TypeScript Integration

```typescript
class DevBoostClient {
  private baseUrl: string;
  private apiUrl: string;

  constructor(baseUrl: string = 'http://localhost:8000') {
    this.baseUrl = baseUrl;
    this.apiUrl = `${baseUrl}/api/v1`;
  }

  async analyze(repo: string, task: string) {
    const response = await fetch(`${this.apiUrl}/analyze`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ repo, task })
    });
    
    if (!response.ok) {
      throw new Error(`API error: ${response.statusText}`);
    }
    
    return await response.json();
  }

  async getTasks() {
    const response = await fetch(`${this.apiUrl}/tasks`);
    return await response.json();
  }

  async healthCheck() {
    const response = await fetch(`${this.apiUrl}/health`);
    return await response.json();
  }
}

// Usage
const client = new DevBoostClient();
const result = await client.analyze(
  'https://github.com/user/repo',
  'explain'
);
console.log(result.result);
```

---

### cURL Examples

```bash
# Get available tasks
curl http://localhost:8000/api/v1/tasks

# Health check
curl http://localhost:8000/api/v1/health

# Analyze repository
curl -X POST http://localhost:8000/api/v1/analyze \
  -H "Content-Type: application/json" \
  -d '{"repo": "https://github.com/user/repo", "task": "explain"}'

# Pretty print JSON response
curl -X POST http://localhost:8000/api/v1/analyze \
  -H "Content-Type: application/json" \
  -d '{"repo": "https://github.com/user/repo", "task": "docs"}' \
  | python -m json.tool
```

---

## 📊 API Response Times

| Endpoint | Average Response Time |
|----------|----------------------|
| GET /api/v1/tasks | < 10ms |
| GET /api/v1/health | < 5ms |
| POST /api/v1/analyze | 50-200ms (without AI) |
| POST /api/v1/analyze | 2-10s (with AI integration) |

---

## 🔄 Versioning

**Current Version:** v1

**API Versioning Strategy:**
- Version included in URL path: `/api/v1/`
- Breaking changes will increment major version: `/api/v2/`
- Backward compatibility maintained for at least 6 months

---

## 🛡️ Security Best Practices

### For Production Deployment:

1. **Enable HTTPS Only**
```python
# Force HTTPS redirect
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
app.add_middleware(HTTPSRedirectMiddleware)
```

2. **Add API Key Authentication**
```python
from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-Key")

async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != os.getenv("API_KEY"):
        raise HTTPException(status_code=403, detail="Invalid API Key")
```

3. **Implement Rate Limiting**
4. **Add Request Validation**
5. **Enable CORS Selectively**
6. **Log All Requests**
7. **Monitor API Usage**

---

## 📚 Additional Resources

- **Interactive Docs:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc
- **GitHub:** https://github.com/Darshan7075/DEVBOST-AI
- **Test Script:** `python test_api.py`

---

## 🤝 Support

For API issues or questions:
1. Check this documentation
2. Review interactive docs at `/docs`
3. Run test script: `python test_api.py`
4. Open GitHub issue

---

**Last Updated:** 2026-05-01  
**API Version:** 1.0.0  
**Status:** ✅ Production Ready (with recommended security enhancements)