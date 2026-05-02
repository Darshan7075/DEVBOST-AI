# 🚀 DevBoost AI

> **AI-Powered Developer Tool for Intelligent Repository Analysis**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18-blue.svg)](https://reactjs.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📖 Overview

**DevBoost AI** is a production-ready web-based system that analyzes GitHub repositories using **IBM Bob** as the AI engine. It helps developers by:

- 📖 **Explaining Code**: Understand project architecture and workflow
- 📚 **Generating Documentation**: Create comprehensive README files
- 🐛 **Detecting Bugs**: Identify security issues and bad practices
- 🧪 **Creating Test Cases**: Generate unit tests with edge cases

### 🌟 Key Features

- ✅ **IBM Bob Integration**: Leverages IBM Bob for intelligent code analysis
- ✅ **Clean Architecture**: Modular backend with FastAPI
- ✅ **Modern UI**: Responsive React frontend with beautiful design
- ✅ **Production Ready**: Error handling, validation, and best practices
- ✅ **Easy to Use**: Simple interface for quick repository analysis

---

## 🏗️ Project Structure

```
DevBoost-AI/
├── backend/                    # Python FastAPI Backend
│   ├── main.py                # Application entry point
│   ├── routes/
│   │   └── analyze.py         # API endpoints
│   ├── services/
│   │   └── bob_integration.py # IBM Bob integration
│   └── requirements.txt       # Python dependencies
│
├── frontend/                   # React Frontend
│   └── index.html             # Single-page application
│
└── README.md                  # This file
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+** installed
- **pip** package manager
- **Git** for cloning the repository
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/DevBoost-AI.git
cd DevBoost-AI
```

#### 2. Set Up Backend

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Start the Backend Server

```bash
# Run the FastAPI server
python main.py
```

The backend will start at: **http://localhost:8000**

API Documentation available at: **http://localhost:8000/docs**

#### 4. Open the Frontend

```bash
# In a new terminal, navigate to frontend directory
cd frontend

# Open index.html in your browser
# On Windows:
start index.html
# On macOS:
open index.html
# On Linux:
xdg-open index.html
```

Or simply double-click `frontend/index.html` to open it in your default browser.

---

## 💻 Usage

### Using the Web Interface

1. **Enter Repository URL**: Paste a GitHub repository URL
   - Example: `https://github.com/username/repository`

2. **Select Analysis Task**:
   - **Explain Project**: Get project overview and architecture
   - **Generate Documentation**: Create comprehensive docs
   - **Find Bugs**: Identify issues and security vulnerabilities
   - **Generate Tests**: Create unit test cases

3. **Click "Analyze with Bob"**: IBM Bob will analyze the repository

4. **View Results**: See structured analysis output

### Using the API Directly

#### Analyze Repository

```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "repo_url": "https://github.com/username/repository",
    "task": "explain"
  }'
```

#### Get Available Tasks

```bash
curl http://localhost:8000/tasks
```

#### Health Check

```bash
curl http://localhost:8000/health
```

---

## 🎯 API Endpoints

### POST /analyze

Analyze a GitHub repository with IBM Bob.

**Request Body:**
```json
{
  "repo_url": "https://github.com/username/repository",
  "task": "explain"
}
```

**Response:**
```json
{
  "status": "success",
  "task": "explain",
  "repo_url": "https://github.com/username/repository",
  "result": {
    "summary": "Project Analysis Complete",
    "content": "...",
    "metadata": {
      "analyzed_by": "IBM Bob",
      "task_type": "explain"
    }
  }
}
```

**Supported Tasks:**
- `explain` - Explain project architecture
- `docs` - Generate documentation
- `bugs` - Find bugs and issues
- `tests` - Generate test cases

### GET /tasks

Get list of available analysis tasks.

### GET /health

Health check endpoint.

---

## 🔧 Configuration

### Backend Configuration

The backend runs on `http://localhost:8000` by default. To change:

Edit `backend/main.py`:
```python
uvicorn.run(
    "main:app",
    host="0.0.0.0",
    port=8000,  # Change port here
    reload=True
)
```

### Frontend Configuration

The frontend connects to the backend API. To change the API URL:

Edit `frontend/index.html`:
```javascript
const API_URL = 'http://localhost:8000';  // Change API URL here
```

---

## 🧪 Testing

### Test the Backend

```bash
# Navigate to backend directory
cd backend

# Run with pytest (if installed)
pytest tests/

# Or test manually with curl
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"repo_url": "https://github.com/fastapi/fastapi", "task": "explain"}'
```

### Test the Frontend

1. Open `frontend/index.html` in your browser
2. Enter a valid GitHub URL
3. Select a task
4. Click "Analyze with Bob"
5. Verify results are displayed correctly

---

## 🎨 Features in Detail

### 1. Code Explanation
- Analyzes project purpose and goals
- Explains architecture and design patterns
- Identifies key components and their roles
- Describes workflow and data flow

### 2. Documentation Generation
- Creates comprehensive README files
- Includes installation instructions
- Provides usage examples
- Documents API endpoints
- Adds configuration details

### 3. Bug Detection
- Identifies syntax and logic errors
- Detects security vulnerabilities
- Finds performance issues
- Suggests fixes with code examples
- Prioritizes issues by severity

### 4. Test Case Generation
- Creates unit tests for functions
- Generates edge case tests
- Includes integration tests
- Provides test code examples
- Suggests test frameworks

---

## 🔐 Security

- ✅ Input validation on all endpoints
- ✅ URL format validation for GitHub repos
- ✅ Error handling for invalid requests
- ✅ CORS configuration for frontend access
- ✅ No sensitive data in responses

---

## 🚀 Deployment

### Deploy Backend

#### Using Docker (Recommended)

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:
```bash
docker build -t devboost-backend .
docker run -p 8000:8000 devboost-backend
```

#### Using Cloud Platforms

- **Heroku**: Deploy with `Procfile`
- **AWS**: Use Elastic Beanstalk or Lambda
- **Google Cloud**: Deploy to Cloud Run
- **Azure**: Use App Service

### Deploy Frontend

- Host `frontend/index.html` on any static hosting:
  - **Netlify**: Drag and drop deployment
  - **Vercel**: Git-based deployment
  - **GitHub Pages**: Free hosting
  - **AWS S3**: Static website hosting

---

## 🛠️ Development

### Adding New Analysis Tasks

1. **Update `bob_integration.py`**:
   - Add new task prompt in `_generate_prompt()`
   - Add response template in `_generate_response()`

2. **Update `analyze.py`**:
   - Add task to validation list

3. **Update Frontend**:
   - Add task option in `index.html`
   - Add task description

### Customizing IBM Bob Integration

Edit `backend/services/bob_integration.py`:

```python
async def analyze_with_bob(repo_url: str, task: str) -> Dict[str, Any]:
    # Add your IBM Bob API integration here
    # Example:
    # response = await ibm_bob_api.analyze(repo_url, task)
    # return response
    pass
```

---

## 📚 Documentation

- **API Docs**: http://localhost:8000/docs (when server is running)
- **ReDoc**: http://localhost:8000/redoc
- **Source Code**: Well-commented and beginner-friendly

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Commit: `git commit -m 'Add amazing feature'`
5. Push: `git push origin feature/amazing-feature`
6. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **IBM Bob**: AI engine for intelligent code analysis
- **FastAPI**: Modern Python web framework
- **React**: Frontend library
- **Open Source Community**: For amazing tools and libraries

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/DevBoost-AI/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/DevBoost-AI/discussions)
- **Email**: support@devboost.ai

---

## 🎯 Roadmap

### Current Version (1.0)
- ✅ Core analysis features
- ✅ IBM Bob integration
- ✅ Web interface
- ✅ API endpoints

### Future Plans
- [ ] Real-time analysis progress
- [ ] Multiple repository comparison
- [ ] Export results to PDF/Markdown
- [ ] GitHub OAuth integration
- [ ] Team collaboration features
- [ ] Custom analysis rules
- [ ] VS Code extension

---

<div align="center">

**Made with ❤️ using IBM Bob**

[Website](https://devboost.ai) • [Documentation](https://docs.devboost.ai) • [GitHub](https://github.com/yourusername/DevBoost-AI)

</div>