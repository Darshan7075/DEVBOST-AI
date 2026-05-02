# 🚀 DevBoost AI - Complete Setup Guide

This guide will walk you through setting up DevBoost AI from scratch.

---

## 📋 Table of Contents

1. [System Requirements](#system-requirements)
2. [Installation Steps](#installation-steps)
3. [Running the Application](#running-the-application)
4. [Troubleshooting](#troubleshooting)
5. [Advanced Configuration](#advanced-configuration)

---

## 💻 System Requirements

### Minimum Requirements
- **Operating System**: Windows 10/11, macOS 10.15+, or Linux
- **Python**: Version 3.10 or higher
- **RAM**: 2GB minimum
- **Disk Space**: 500MB free space
- **Browser**: Chrome, Firefox, Safari, or Edge (latest version)

### Recommended
- **Python**: 3.11+
- **RAM**: 4GB or more
- **Internet**: Stable connection for GitHub API access

---

## 🔧 Installation Steps

### Step 1: Install Python

#### Windows
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. ✅ **Important**: Check "Add Python to PATH"
4. Click "Install Now"
5. Verify installation:
   ```bash
   python --version
   ```

#### macOS
```bash
# Using Homebrew
brew install python@3.11

# Verify installation
python3 --version
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3.11 python3-pip python3-venv

# Verify installation
python3 --version
```

### Step 2: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/yourusername/DevBoost-AI.git

# Navigate to project directory
cd DevBoost-AI
```

### Step 3: Set Up Backend

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows (Command Prompt):
venv\Scripts\activate.bat

# Windows (PowerShell):
venv\Scripts\Activate.ps1

# macOS/Linux:
source venv/bin/activate

# You should see (venv) in your terminal prompt

# Install dependencies
pip install -r requirements.txt

# Verify installation
pip list
```

### Step 4: Verify Backend Setup

```bash
# Test the backend
python main.py
```

You should see:
```
======================================================================
🚀 Starting DevBoost AI Backend Server
======================================================================

📚 API Documentation: http://localhost:8000/docs
🏠 API Root: http://localhost:8000

⚡ Press CTRL+C to stop the server
```

Keep this terminal open!

### Step 5: Open Frontend

**Option 1: Double-click**
- Navigate to the `frontend` folder
- Double-click `index.html`

**Option 2: Command Line**
```bash
# In a NEW terminal (keep backend running)
cd frontend

# Windows
start index.html

# macOS
open index.html

# Linux
xdg-open index.html
```

---

## 🎮 Running the Application

### Starting the Backend

```bash
# Navigate to backend directory
cd backend

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Start server
python main.py
```

**Backend will be available at:**
- API: http://localhost:8000
- Docs: http://localhost:8000/docs
- Health: http://localhost:8000/health

### Opening the Frontend

Simply open `frontend/index.html` in your browser.

### Using the Application

1. **Enter GitHub URL**
   ```
   Example: https://github.com/fastapi/fastapi
   ```

2. **Select Task**
   - Explain Project
   - Generate Documentation
   - Find Bugs
   - Generate Tests

3. **Click "Analyze with Bob"**

4. **View Results**

---

## 🔍 Troubleshooting

### Common Issues

#### Issue 1: "Python not found"

**Solution:**
```bash
# Windows - Add Python to PATH
# 1. Search "Environment Variables" in Start Menu
# 2. Click "Environment Variables"
# 3. Under "System Variables", find "Path"
# 4. Add Python installation directory

# Verify
python --version
```

#### Issue 2: "pip not found"

**Solution:**
```bash
# Windows
python -m ensurepip --upgrade

# macOS/Linux
python3 -m ensurepip --upgrade
```

#### Issue 3: "Module not found" errors

**Solution:**
```bash
# Make sure virtual environment is activated
# You should see (venv) in terminal

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

#### Issue 4: "Port 8000 already in use"

**Solution:**
```bash
# Option 1: Kill process using port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux:
lsof -ti:8000 | xargs kill -9

# Option 2: Change port in main.py
# Edit backend/main.py, line with uvicorn.run():
uvicorn.run("main:app", host="0.0.0.0", port=8001)  # Use 8001
```

#### Issue 5: CORS errors in browser

**Solution:**
- Make sure backend is running
- Check that API_URL in frontend/index.html matches backend URL
- Clear browser cache and reload

#### Issue 6: "Cannot activate virtual environment" (Windows PowerShell)

**Solution:**
```powershell
# Run PowerShell as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then try activating again
venv\Scripts\Activate.ps1
```

#### Issue 7: Frontend shows "Network Error"

**Checklist:**
- ✅ Backend is running (check http://localhost:8000)
- ✅ No firewall blocking port 8000
- ✅ API_URL in frontend matches backend URL
- ✅ Browser console shows no CORS errors

---

## ⚙️ Advanced Configuration

### Changing Backend Port

Edit `backend/main.py`:
```python
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,  # Change to your preferred port
        reload=True
    )
```

Then update frontend `index.html`:
```javascript
const API_URL = 'http://localhost:8080';  // Match backend port
```

### Running Backend in Production Mode

```bash
# Disable auto-reload for production
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Using Environment Variables

Create `.env` file in backend directory:
```env
# Backend Configuration
HOST=0.0.0.0
PORT=8000
DEBUG=false

# IBM Bob Configuration (when available)
IBM_BOB_API_KEY=your_api_key_here
IBM_BOB_ENDPOINT=https://api.ibm.com/bob
```

Load in `main.py`:
```python
from dotenv import load_dotenv
import os

load_dotenv()

PORT = int(os.getenv('PORT', 8000))
```

### Enabling HTTPS (Production)

```bash
# Generate self-signed certificate (development only)
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes

# Run with HTTPS
uvicorn main:app --host 0.0.0.0 --port 443 --ssl-keyfile=key.pem --ssl-certfile=cert.pem
```

### Running as Background Service

#### Windows (using NSSM)
```bash
# Download NSSM from nssm.cc
nssm install DevBoostAI "C:\path\to\venv\Scripts\python.exe" "C:\path\to\backend\main.py"
nssm start DevBoostAI
```

#### Linux (using systemd)
Create `/etc/systemd/system/devboost.service`:
```ini
[Unit]
Description=DevBoost AI Backend
After=network.target

[Service]
Type=simple
User=youruser
WorkingDirectory=/path/to/backend
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/python main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable devboost
sudo systemctl start devboost
sudo systemctl status devboost
```

---

## 🧪 Testing Your Setup

### Test Backend API

```bash
# Test health endpoint
curl http://localhost:8000/health

# Expected response:
# {"status":"healthy","service":"DevBoost AI Backend"}

# Test analyze endpoint
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"repo_url":"https://github.com/fastapi/fastapi","task":"explain"}'
```

### Test Frontend

1. Open http://localhost:8000/docs in browser
2. Try the interactive API documentation
3. Open frontend/index.html
4. Enter a GitHub URL and test analysis

---

## 📊 Performance Optimization

### Backend Optimization

```python
# Use multiple workers for production
uvicorn main:app --workers 4 --host 0.0.0.0 --port 8000

# Enable caching (add to main.py)
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="devboost-cache")
```

### Frontend Optimization

- Minify JavaScript and CSS for production
- Use CDN for React and Axios
- Enable browser caching
- Compress images and assets

---

## 🔒 Security Best Practices

1. **Never commit sensitive data**
   - Use `.env` files for secrets
   - Add `.env` to `.gitignore`

2. **Validate all inputs**
   - Already implemented in backend

3. **Use HTTPS in production**
   - Get SSL certificate from Let's Encrypt

4. **Rate limiting**
   ```python
   from slowapi import Limiter
   
   limiter = Limiter(key_func=get_remote_address)
   app.state.limiter = limiter
   
   @app.post("/analyze")
   @limiter.limit("10/minute")
   async def analyze(...):
       ...
   ```

5. **Keep dependencies updated**
   ```bash
   pip list --outdated
   pip install --upgrade package_name
   ```

---

## 📞 Getting Help

If you encounter issues:

1. **Check logs**: Look at terminal output for errors
2. **Search issues**: Check GitHub Issues
3. **Ask for help**: Open a new issue with:
   - Your OS and Python version
   - Error message
   - Steps to reproduce

---

## ✅ Setup Checklist

- [ ] Python 3.10+ installed
- [ ] Repository cloned
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] Backend starts successfully
- [ ] Frontend opens in browser
- [ ] Can analyze a repository
- [ ] API documentation accessible

---

## 🎉 Next Steps

Once setup is complete:

1. Read the [README.md](README.md) for usage instructions
2. Explore the API documentation at http://localhost:8000/docs
3. Try analyzing different repositories
4. Customize the prompts in `bob_integration.py`
5. Deploy to production (see README.md)

---

<div align="center">

**Setup Complete! 🎊**

You're ready to use DevBoost AI!

[Back to README](README.md) • [Report Issue](https://github.com/yourusername/DevBoost-AI/issues)

</div>