# 🔧 DevBoost AI - Troubleshooting Guide

Common issues and their solutions.

---

## 🐛 Installation Issues

### Issue: "ModuleNotFoundError: No module named 'fastapi'"

**Cause**: Dependencies not installed

**Solution**:
```bash
# Make sure you're in the backend directory
cd backend

# Make sure virtual environment is activated
# You should see (venv) in your terminal

# Install dependencies
pip install -r requirements.txt

# Verify installation
python test_installation.py
```

### Issue: "pip not found"

**Solution**:
```bash
# Windows
python -m ensurepip --upgrade
python -m pip install --upgrade pip

# Mac/Linux
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip
```

### Issue: Virtual environment activation fails (Windows PowerShell)

**Error**: "cannot be loaded because running scripts is disabled"

**Solution**:
```powershell
# Run PowerShell as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate again
venv\Scripts\Activate.ps1
```

### Issue: Installation takes too long or hangs

**Solution**:
```bash
# Use a faster mirror
pip install -r requirements.txt --index-url https://pypi.org/simple

# Or install with no cache
pip install -r requirements.txt --no-cache-dir

# Or upgrade pip first
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🚀 Server Issues

### Issue: "Port 8000 already in use"

**Solution**:

**Windows**:
```bash
# Find process using port 8000
netstat -ano | findstr :8000

# Kill the process (replace PID with actual process ID)
taskkill /PID <PID> /F
```

**Mac/Linux**:
```bash
# Find and kill process
lsof -ti:8000 | xargs kill -9

# Or use a different port
# Edit backend/main.py and change port to 8001
```

### Issue: "Address already in use"

**Solution**:
```bash
# Option 1: Kill existing process (see above)

# Option 2: Use different port
# Edit backend/main.py:
uvicorn.run("main:app", host="0.0.0.0", port=8001)

# Update frontend/index.html:
const API_URL = 'http://localhost:8001';
```

### Issue: Server starts but shows errors

**Check**:
1. All dependencies installed: `pip list`
2. Python version: `python --version` (should be 3.10+)
3. Virtual environment activated: Look for `(venv)` in terminal
4. No syntax errors in code files

---

## 🌐 Frontend Issues

### Issue: "Network Error" or "Failed to fetch"

**Checklist**:
- ✅ Backend is running (check http://localhost:8000)
- ✅ No firewall blocking port 8000
- ✅ API_URL in frontend matches backend URL
- ✅ CORS is configured (already done in main.py)

**Solution**:
```bash
# Test backend directly
curl http://localhost:8000/health

# Should return: {"status":"healthy","service":"DevBoost AI Backend"}
```

### Issue: CORS errors in browser console

**Error**: "Access-Control-Allow-Origin"

**Solution**: Already configured in `backend/main.py`, but verify:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # This allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Issue: Frontend doesn't load or shows blank page

**Solution**:
1. Open browser console (F12)
2. Check for JavaScript errors
3. Verify React and Axios are loading from CDN
4. Try different browser
5. Clear browser cache

---

## 🔍 API Issues

### Issue: "Invalid GitHub URL format"

**Cause**: URL validation is strict

**Valid formats**:
```
✅ https://github.com/username/repository
✅ https://github.com/fastapi/fastapi
✅ https://github.com/user-name/repo-name

❌ github.com/username/repository (missing https://)
❌ https://github.com/username (missing repository)
❌ http://github.com/username/repository (http instead of https)
```

### Issue: "Invalid task type"

**Valid tasks**:
- `explain` - Explain project
- `docs` - Generate documentation
- `bugs` - Find bugs
- `tests` - Generate tests

**Check spelling**: Task names are case-sensitive and lowercase

---

## 🐍 Python Issues

### Issue: "Python not found"

**Windows**:
1. Download from [python.org](https://www.python.org/downloads/)
2. Run installer
3. ✅ Check "Add Python to PATH"
4. Restart terminal
5. Verify: `python --version`

**Mac**:
```bash
# Using Homebrew
brew install python@3.11

# Verify
python3 --version
```

**Linux**:
```bash
sudo apt update
sudo apt install python3.11 python3-pip python3-venv

# Verify
python3 --version
```

### Issue: Wrong Python version

**Check version**:
```bash
python --version
# Should be 3.10 or higher
```

**Solution**: Install correct version or use:
```bash
# If you have multiple Python versions
python3.11 -m venv venv
```

---

## 📦 Dependency Issues

### Issue: "No matching distribution found"

**Solution**:
```bash
# Update pip
python -m pip install --upgrade pip

# Try installing again
pip install -r requirements.txt

# Or install packages individually
pip install fastapi uvicorn pydantic
```

### Issue: "ERROR: Could not build wheels"

**Solution**:
```bash
# Install build tools
# Windows: Install Visual C++ Build Tools
# Mac: xcode-select --install
# Linux: sudo apt install build-essential

# Then try again
pip install -r requirements.txt
```

---

## 🔒 Permission Issues

### Issue: "Permission denied"

**Windows**:
```bash
# Run terminal as Administrator
# Or use:
pip install --user -r requirements.txt
```

**Mac/Linux**:
```bash
# Don't use sudo with virtual environment
# Make sure venv is activated

# If needed:
chmod +x backend/start.py
```

---

## 🧪 Testing Issues

### Issue: Can't test the API

**Solution**:
```bash
# Test with curl
curl http://localhost:8000/health

# Test analyze endpoint
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"repo_url":"https://github.com/fastapi/fastapi","task":"explain"}'

# Or use the interactive docs
# Open: http://localhost:8000/docs
```

---

## 💡 Quick Fixes

### Reset Everything

```bash
# 1. Deactivate virtual environment
deactivate

# 2. Delete virtual environment
# Windows:
rmdir /s venv
# Mac/Linux:
rm -rf venv

# 3. Create new virtual environment
python -m venv venv

# 4. Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 5. Install dependencies
pip install -r requirements.txt

# 6. Test
python test_installation.py
```

### Verify Installation

```bash
# Run test script
cd backend
python test_installation.py

# Should show:
# ✅ FastAPI imported successfully
# ✅ Uvicorn imported successfully
# ✅ Pydantic imported successfully
# etc.
```

---

## 🆘 Still Having Issues?

### Collect Information

Before asking for help, collect:

1. **Python version**: `python --version`
2. **Operating System**: Windows/Mac/Linux version
3. **Error message**: Full error text
4. **What you tried**: Steps you've taken
5. **Terminal output**: Copy relevant output

### Get Help

1. Check [SETUP_GUIDE.md](SETUP_GUIDE.md)
2. Review [README.md](README.md)
3. Search existing issues on GitHub
4. Open a new issue with collected information

### Debug Mode

Enable detailed logging:

```python
# Edit backend/main.py
import logging
logging.basicConfig(level=logging.DEBUG)

# Run server
python main.py
```

---

## ✅ Verification Checklist

Before reporting an issue, verify:

- [ ] Python 3.10+ installed
- [ ] Virtual environment created
- [ ] Virtual environment activated (see `(venv)` in terminal)
- [ ] Dependencies installed (`pip list` shows packages)
- [ ] In correct directory (`backend/` for server)
- [ ] No other process using port 8000
- [ ] Firewall not blocking connections
- [ ] Using correct Python command (`python` or `python3`)

---

## 📞 Common Commands Reference

```bash
# Check Python version
python --version

# Check pip version
pip --version

# List installed packages
pip list

# Check if package is installed
pip show fastapi

# Upgrade pip
python -m pip install --upgrade pip

# Install specific package
pip install fastapi

# Uninstall package
pip uninstall fastapi

# Check port usage (Windows)
netstat -ano | findstr :8000

# Check port usage (Mac/Linux)
lsof -i :8000

# Test API
curl http://localhost:8000/health
```

---

<div align="center">

**Still stuck? Don't worry!**

[Back to README](README.md) • [Setup Guide](SETUP_GUIDE.md) • [Report Issue](https://github.com/yourusername/DevBoost-AI/issues)

</div>