"""
DevBoost AI - Easy Startup Script
Run this to start the backend server
"""

import sys
import subprocess

def check_dependencies():
    """Check if all dependencies are installed"""
    try:
        import fastapi
        import uvicorn
        import pydantic
        return True
    except ImportError:
        print("❌ Dependencies not installed!")
        print("\nPlease run: pip install -r requirements.txt")
        return False

def start_server():
    """Start the FastAPI server"""
    if not check_dependencies():
        sys.exit(1)
    
    print("=" * 70)
    print("🚀 Starting DevBoost AI Backend Server")
    print("=" * 70)
    print("\n📚 API Documentation: http://localhost:8000/docs")
    print("🏠 API Root: http://localhost:8000")
    print("💚 Health Check: http://localhost:8000/health")
    print("\n⚡ Press CTRL+C to stop the server\n")
    print("=" * 70)
    
    # Import and run
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    start_server()

# Made with Bob
