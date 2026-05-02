"""
DevBoost AI - Backend Server
Production-ready FastAPI application for AI-powered repository analysis
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

from routes.analyze import router as analyze_router

# Create FastAPI application
app = FastAPI(
    title="DevBoost AI",
    description="AI-Powered Developer Tool for Repository Analysis",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(analyze_router)


@app.get("/")
async def root():
    """Root endpoint - API information"""
    return {
        "service": "DevBoost AI",
        "version": "1.0.0",
        "description": "AI-Powered Developer Tool",
        "status": "running",
        "endpoints": {
            "analyze": "/analyze",
            "health": "/health",
            "docs": "/docs"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "DevBoost AI Backend"
    }


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler for unhandled errors"""
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "detail": str(exc),
            "type": type(exc).__name__
        }
    )


if __name__ == "__main__":
    print("=" * 70)
    print("🚀 Starting DevBoost AI Backend Server")
    print("=" * 70)
    print("\n📚 API Documentation: http://localhost:8000/docs")
    print("🏠 API Root: http://localhost:8000")
    print("\n⚡ Press CTRL+C to stop the server\n")
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

# Made with Bob
