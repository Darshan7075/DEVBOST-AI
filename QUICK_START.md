# ⚡ DevBoost AI - Quick Start Guide

Get up and running in 5 minutes!

---

## 🎯 What You'll Need

- Python 3.10+ installed
- A web browser
- 5 minutes of your time

---

## 🚀 Installation (3 Steps)

### Step 1: Get the Code

```bash
git clone https://github.com/yourusername/DevBoost-AI.git
cd DevBoost-AI
```

### Step 2: Set Up Backend

```bash
cd backend
python -m venv venv

# Activate virtual environment:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### Step 3: Start the Server

```bash
python main.py
```

✅ Backend is now running at http://localhost:8000

---

## 🎨 Open the Frontend

**Option 1**: Double-click `frontend/index.html`

**Option 2**: Command line
```bash
# Windows
start frontend/index.html

# Mac
open frontend/index.html

# Linux
xdg-open frontend/index.html
```

---

## 🎮 Try It Out!

1. **Enter a GitHub URL**:
   ```
   https://github.com/fastapi/fastapi
   ```

2. **Select a task**:
   - Explain Project
   - Generate Documentation
   - Find Bugs
   - Generate Tests

3. **Click "Analyze with Bob"**

4. **View the results!** 🎉

---

## 🐛 Troubleshooting

### "Python not found"
```bash
# Check if Python is installed
python --version

# If not, download from python.org
```

### "Port 8000 already in use"
```bash
# Kill the process
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Mac/Linux:
lsof -ti:8000 | xargs kill -9
```

### "Module not found"
```bash
# Make sure virtual environment is activated
# You should see (venv) in your terminal

# Reinstall dependencies
pip install -r requirements.txt
```

---

## 📚 Next Steps

- Read the full [README.md](README.md)
- Check out [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed instructions
- Explore the API docs at http://localhost:8000/docs

---

## 💡 Example Usage

### Analyze FastAPI Repository

```bash
# Using curl
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "repo_url": "https://github.com/fastapi/fastapi",
    "task": "explain"
  }'
```

### Get Available Tasks

```bash
curl http://localhost:8000/tasks
```

---

## ✅ Verification Checklist

- [ ] Python 3.10+ installed
- [ ] Repository cloned
- [ ] Virtual environment activated
- [ ] Dependencies installed
- [ ] Backend running (http://localhost:8000)
- [ ] Frontend opens in browser
- [ ] Successfully analyzed a repository

---

<div align="center">

**You're all set! 🎊**

Happy coding with DevBoost AI!

[Full Documentation](README.md) • [Detailed Setup](SETUP_GUIDE.md) • [Report Issues](https://github.com/yourusername/DevBoost-AI/issues)

</div>