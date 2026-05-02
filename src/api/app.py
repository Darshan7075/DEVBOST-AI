"""
FastAPI Application for DevBoost AI
Main application entry point for the API server
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from api.routes import router


# Create FastAPI app
app = FastAPI(
    title="DevBoost AI API",
    description="AI-Powered Development Assistant API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(router)


@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
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


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler"""
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "detail": str(exc)
        }
    )


if __name__ == "__main__":
    import uvicorn
    
    print("=" * 70)
    print("Starting DevBoost AI API Server")
    print("=" * 70)
    print("\nAPI Documentation: http://localhost:8000/docs")
    print("API Root: http://localhost:8000")
    print("\nPress CTRL+C to stop the server\n")
    
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

# Made with Bob
