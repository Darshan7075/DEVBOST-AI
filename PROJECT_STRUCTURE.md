# 📁 DevBoost AI - Project Structure

Complete overview of the project architecture and file organization.

---

## 🏗️ Directory Structure

```
DevBoost-AI/
│
├── backend/                          # Backend API Server
│   ├── main.py                       # FastAPI application entry point
│   ├── requirements.txt              # Python dependencies
│   │
│   ├── routes/                       # API route handlers
│   │   └── analyze.py                # Analysis endpoints
│   │
│   └── services/                     # Business logic layer
│       └── bob_integration.py        # IBM Bob integration service
│
├── frontend/                         # Frontend Application
│   └── index.html                    # Single-page React application
│
├── README.md                         # Main documentation
├── SETUP_GUIDE.md                    # Installation and setup guide
└── PROJECT_STRUCTURE.md              # This file
```

---

## 📄 File Descriptions

### Backend Files

#### `backend/main.py`
**Purpose**: Main application entry point and FastAPI configuration

**Key Components**:
- FastAPI app initialization
- CORS middleware configuration
- Router registration
- Global exception handler
- Server startup configuration

**Code Structure**:
```python
app = FastAPI(...)           # Create app
app.add_middleware(...)      # Configure CORS
app.include_router(...)      # Register routes
@app.get("/")               # Root endpoint
@app.get("/health")         # Health check
@app.exception_handler(...) # Error handling
```

**Usage**:
```bash
python main.py  # Start server
```

---

#### `backend/routes/analyze.py`
**Purpose**: API endpoints for repository analysis

**Key Components**:
- Request/Response models (Pydantic)
- Input validation
- Route handlers
- Error handling

**Endpoints**:
- `POST /analyze` - Analyze repository
- `GET /tasks` - Get available tasks
- `GET /health` - Health check

**Request Model**:
```python
class AnalyzeRequest(BaseModel):
    repo_url: str  # GitHub URL
    task: str      # Analysis task type
```

**Validation**:
- GitHub URL format validation
- Task type validation
- Empty input checks

---

#### `backend/services/bob_integration.py`
**Purpose**: IBM Bob integration and prompt generation

**Key Functions**:

1. **`analyze_with_bob(repo_url, task)`**
   - Main integration function
   - Generates prompts
   - Processes with IBM Bob
   - Returns structured results

2. **`_generate_prompt(repo_url, task)`**
   - Creates task-specific prompts
   - Leverages IBM Bob's capabilities
   - Structured for optimal results

3. **`_generate_response(repo_url, task, prompt)`**
   - Generates formatted responses
   - Task-specific output structure
   - Includes metadata

**Supported Tasks**:
- `explain` - Project explanation
- `docs` - Documentation generation
- `bugs` - Bug detection
- `tests` - Test case generation

**Response Structure**:
```python
{
    "summary": "...",
    "content": "...",
    "metadata": {
        "analyzed_by": "IBM Bob",
        "task_type": "...",
        ...
    }
}
```

---

#### `backend/requirements.txt`
**Purpose**: Python package dependencies

**Core Dependencies**:
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `pydantic` - Data validation
- `httpx` - HTTP client
- `aiohttp` - Async HTTP

**Optional Dependencies**:
- `pytest` - Testing
- `black` - Code formatting
- `ruff` - Linting

---

### Frontend Files

#### `frontend/index.html`
**Purpose**: Complete single-page React application

**Key Components**:

1. **HTML Structure**
   - Responsive layout
   - Modern styling
   - Semantic markup

2. **CSS Styling**
   - Gradient background
   - Card-based design
   - Animations
   - Responsive design
   - Dark theme elements

3. **React Application**
   - Functional components
   - State management (useState)
   - Form handling
   - API integration (Axios)
   - Error handling
   - Loading states

**State Variables**:
```javascript
const [repoUrl, setRepoUrl] = useState('')
const [task, setTask] = useState('explain')
const [loading, setLoading] = useState(false)
const [error, setError] = useState(null)
const [result, setResult] = useState(null)
```

**Features**:
- Real-time task descriptions
- Loading spinner
- Error display
- Formatted results
- Responsive design
- Beautiful animations

---

### Documentation Files

#### `README.md`
**Purpose**: Main project documentation

**Sections**:
- Project overview
- Features
- Quick start guide
- Installation instructions
- Usage examples
- API documentation
- Deployment guide
- Contributing guidelines

---

#### `SETUP_GUIDE.md`
**Purpose**: Detailed setup instructions

**Sections**:
- System requirements
- Step-by-step installation
- Running the application
- Troubleshooting
- Advanced configuration
- Performance optimization
- Security best practices

---

#### `PROJECT_STRUCTURE.md`
**Purpose**: Architecture documentation (this file)

**Sections**:
- Directory structure
- File descriptions
- Code organization
- Data flow
- Integration points

---

## 🔄 Data Flow

### Request Flow

```
User Input (Frontend)
    ↓
Frontend Form Submission
    ↓
Axios POST Request
    ↓
Backend API (/analyze)
    ↓
Request Validation (Pydantic)
    ↓
Bob Integration Service
    ↓
Prompt Generation
    ↓
IBM Bob Processing
    ↓
Response Formatting
    ↓
JSON Response
    ↓
Frontend Display
    ↓
User Views Results
```

### Component Interaction

```
┌─────────────────────────────────────────┐
│           Frontend (React)              │
│  - User Interface                       │
│  - Form Handling                        │
│  - Result Display                       │
└──────────────┬──────────────────────────┘
               │ HTTP Request
               ↓
┌─────────────────────────────────────────┐
│        Backend API (FastAPI)            │
│  ┌───────────────────────────────────┐  │
│  │  Routes (analyze.py)              │  │
│  │  - Endpoint handlers              │  │
│  │  - Validation                     │  │
│  └──────────┬────────────────────────┘  │
│             ↓                            │
│  ┌───────────────────────────────────┐  │
│  │  Services (bob_integration.py)    │  │
│  │  - IBM Bob integration            │  │
│  │  - Prompt generation              │  │
│  │  - Response formatting            │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

---

## 🎯 Design Patterns

### Backend Architecture

**Pattern**: Layered Architecture

1. **Presentation Layer** (`routes/`)
   - API endpoints
   - Request/response handling
   - Input validation

2. **Business Logic Layer** (`services/`)
   - Core functionality
   - IBM Bob integration
   - Data processing

3. **Data Layer** (Future)
   - Database operations
   - Caching
   - External APIs

### Frontend Architecture

**Pattern**: Component-Based Architecture

- Single-page application
- State management with hooks
- Separation of concerns
- Reusable components

---

## 🔌 Integration Points

### IBM Bob Integration

**Location**: `backend/services/bob_integration.py`

**Integration Method**:
```python
async def analyze_with_bob(repo_url: str, task: str):
    # 1. Generate prompt
    prompt = _generate_prompt(repo_url, task)
    
    # 2. Call IBM Bob API (placeholder)
    # response = await ibm_bob_api.analyze(prompt)
    
    # 3. Format response
    result = _generate_response(repo_url, task, prompt)
    
    return result
```

**To Add Real IBM Bob API**:
1. Get IBM Bob API credentials
2. Install IBM SDK: `pip install ibm-watson`
3. Replace mock implementation with actual API calls
4. Add error handling for API failures

---

## 📦 Dependencies

### Backend Dependencies

```
fastapi==0.104.1          # Web framework
uvicorn==0.24.0           # ASGI server
pydantic==2.5.0           # Data validation
httpx==0.25.2             # HTTP client
aiohttp==3.9.1            # Async HTTP
python-dotenv==1.0.0      # Environment variables
```

### Frontend Dependencies (CDN)

```
React 18                  # UI library
ReactDOM 18               # React DOM
Babel Standalone          # JSX transpiler
Axios                     # HTTP client
```

---

## 🚀 Extending the Project

### Adding New Analysis Tasks

1. **Update `bob_integration.py`**:
```python
# Add to _generate_prompt()
task_prompts = {
    "new_task": base_prompt + """
    Your new task instructions here
    """
}

# Add to _generate_response()
responses = {
    "new_task": {
        "summary": "...",
        "content": "...",
        "metadata": {...}
    }
}
```

2. **Update `analyze.py`**:
```python
@validator('task')
def validate_task(cls, v):
    valid_tasks = ['explain', 'docs', 'bugs', 'tests', 'new_task']
    # ...
```

3. **Update Frontend**:
```html
<select id="task">
    <option value="new_task">New Task - Description</option>
</select>
```

### Adding Database Support

1. Install SQLAlchemy:
```bash
pip install sqlalchemy asyncpg
```

2. Create models:
```python
# backend/models/analysis.py
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Analysis(Base):
    __tablename__ = "analyses"
    id = Column(String, primary_key=True)
    repo_url = Column(String)
    task = Column(String)
    result = Column(String)
    created_at = Column(DateTime)
```

3. Add database layer:
```python
# backend/services/database.py
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine("postgresql://...")
```

### Adding Authentication

1. Install dependencies:
```bash
pip install python-jose[cryptography] passlib[bcrypt]
```

2. Create auth service:
```python
# backend/services/auth.py
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Verify token
    # Return user
    pass
```

3. Protect routes:
```python
@router.post("/analyze")
async def analyze(
    request: AnalyzeRequest,
    user = Depends(get_current_user)
):
    # Only authenticated users can analyze
    pass
```

---

## 🧪 Testing Structure

### Backend Tests (Future)

```
backend/
├── tests/
│   ├── __init__.py
│   ├── test_routes.py          # API endpoint tests
│   ├── test_bob_integration.py # Service tests
│   └── test_validation.py      # Input validation tests
```

### Frontend Tests (Future)

```
frontend/
├── tests/
│   ├── App.test.js             # Component tests
│   ├── api.test.js             # API integration tests
│   └── validation.test.js      # Form validation tests
```

---

## 📊 Performance Considerations

### Backend Optimization

- **Async/Await**: All I/O operations are async
- **Connection Pooling**: For database connections
- **Caching**: Redis for frequently accessed data
- **Rate Limiting**: Prevent API abuse

### Frontend Optimization

- **Code Splitting**: Load components on demand
- **Lazy Loading**: Defer non-critical resources
- **Caching**: Browser caching for static assets
- **Minification**: Compress JS/CSS for production

---

## 🔒 Security Considerations

### Backend Security

- ✅ Input validation (Pydantic)
- ✅ CORS configuration
- ✅ Error handling
- ✅ URL validation
- 🔄 Rate limiting (to be added)
- 🔄 Authentication (to be added)

### Frontend Security

- ✅ XSS prevention (React escaping)
- ✅ HTTPS in production
- ✅ No sensitive data in client
- ✅ Secure API communication

---

## 📝 Code Style

### Backend (Python)

- **Style Guide**: PEP 8
- **Formatter**: Black
- **Linter**: Ruff
- **Type Hints**: Required
- **Docstrings**: Google style

### Frontend (JavaScript)

- **Style Guide**: Airbnb
- **Formatter**: Prettier
- **Linter**: ESLint
- **Comments**: JSDoc style

---

<div align="center">

**Project Structure Documentation Complete**

[Back to README](README.md) • [Setup Guide](SETUP_GUIDE.md)

</div>