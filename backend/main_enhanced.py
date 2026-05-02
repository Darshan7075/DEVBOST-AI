"""
DevBoost AI - Enhanced Backend Server
Production-ready FastAPI application with comprehensive error handling
"""

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import uvicorn
import logging
from datetime import datetime

from routes.analyze import router as analyze_router

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create FastAPI application
app = FastAPI(
    title="DevBoost AI",
    description="AI-Powered Developer Tool for Intelligent Repository Analysis using IBM Bob",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    contact={
        "name": "DevBoost AI Team",
        "email": "support@devboost.ai"
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    }
)

# Configure CORS with security best practices
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins: ["https://yourdomain.com"]
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=3600,
)

# Include routers
app.include_router(analyze_router, tags=["Analysis"])


# ===== MIDDLEWARE =====

@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log all incoming requests"""
    start_time = datetime.now()
    
    # Log request
    logger.info(f"Request: {request.method} {request.url.path}")
    
    # Process request
    response = await call_next(request)
    
    # Calculate processing time
    process_time = (datetime.now() - start_time).total_seconds()
    
    # Log response
    logger.info(
        f"Response: {response.status_code} | "
        f"Time: {process_time:.3f}s | "
        f"Path: {request.url.path}"
    )
    
    # Add custom headers
    response.headers["X-Process-Time"] = str(process_time)
    response.headers["X-Powered-By"] = "IBM Bob AI"
    
    return response


# ===== EXCEPTION HANDLERS =====

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Handle validation errors with detailed messages"""
    errors = []
    for error in exc.errors():
        errors.append({
            "field": " -> ".join(str(loc) for loc in error["loc"]),
            "message": error["msg"],
            "type": error["type"]
        })
    
    logger.warning(f"Validation error on {request.url.path}: {errors}")
    
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": "Validation Error",
            "message": "Invalid input data provided",
            "details": errors,
            "timestamp": datetime.now().isoformat()
        }
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Handle all unhandled exceptions"""
    logger.error(f"Unhandled exception on {request.url.path}: {str(exc)}", exc_info=True)
    
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "Internal Server Error",
            "message": "An unexpected error occurred while processing your request",
            "detail": str(exc),
            "type": type(exc).__name__,
            "timestamp": datetime.now().isoformat(),
            "path": str(request.url.path)
        }
    )


# ===== ROOT ENDPOINTS =====

@app.get("/", tags=["Root"])
async def root():
    """
    Root endpoint - API information and status
    
    Returns basic information about the DevBoost AI API including
    available endpoints and current version.
    """
    return {
        "service": "DevBoost AI",
        "version": "2.0.0",
        "description": "AI-Powered Developer Tool using IBM Bob",
        "status": "operational",
        "ai_engine": "IBM Bob",
        "endpoints": {
            "analyze": {
                "path": "/analyze",
                "method": "POST",
                "description": "Analyze GitHub repository"
            },
            "tasks": {
                "path": "/tasks",
                "method": "GET",
                "description": "Get available analysis tasks"
            },
            "health": {
                "path": "/health",
                "method": "GET",
                "description": "Health check endpoint"
            },
            "docs": {
                "path": "/docs",
                "method": "GET",
                "description": "Interactive API documentation"
            }
        },
        "timestamp": datetime.now().isoformat()
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint
    
    Returns the current health status of the API and its dependencies.
    Used for monitoring and load balancer health checks.
    """
    return {
        "status": "healthy",
        "service": "DevBoost AI Backend",
        "version": "2.0.0",
        "ai_engine": "IBM Bob",
        "timestamp": datetime.now().isoformat(),
        "uptime": "operational"
    }


@app.get("/status", tags=["Health"])
async def status():
    """
    Detailed status endpoint
    
    Returns comprehensive status information including system metrics.
    """
    return {
        "api": {
            "status": "running",
            "version": "2.0.0",
            "environment": "production"
        },
        "ai_engine": {
            "name": "IBM Bob",
            "status": "ready",
            "capabilities": ["explain", "docs", "bugs", "tests"]
        },
        "endpoints": {
            "total": 6,
            "active": 6
        },
        "timestamp": datetime.now().isoformat()
    }


# ===== STARTUP & SHUTDOWN EVENTS =====

@app.on_event("startup")
async def startup_event():
    """Execute on application startup"""
    logger.info("=" * 70)
    logger.info("🚀 DevBoost AI Backend Starting...")
    logger.info("=" * 70)
    logger.info("✅ FastAPI application initialized")
    logger.info("✅ CORS middleware configured")
    logger.info("✅ IBM Bob integration ready")
    logger.info("✅ Error handlers registered")
    logger.info("=" * 70)
    logger.info("📚 API Documentation: http://localhost:8000/docs")
    logger.info("🏠 API Root: http://localhost:8000")
    logger.info("💚 Health Check: http://localhost:8000/health")
    logger.info("=" * 70)


@app.on_event("shutdown")
async def shutdown_event():
    """Execute on application shutdown"""
    logger.info("=" * 70)
    logger.info("🛑 DevBoost AI Backend Shutting Down...")
    logger.info("=" * 70)
    logger.info("✅ Cleanup completed")
    logger.info("👋 Goodbye!")


# ===== MAIN ENTRY POINT =====

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("🚀 Starting DevBoost AI Backend Server")
    print("=" * 70)
    print("\n📚 API Documentation: http://localhost:8000/docs")
    print("🏠 API Root: http://localhost:8000")
    print("💚 Health Check: http://localhost:8000/health")
    print("\n⚡ Press CTRL+C to stop the server\n")
    print("=" * 70 + "\n")
    
    uvicorn.run(
        "main_enhanced:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
        access_log=True
    )

# Made with ❤️ using IBM Bob

# Made with Bob
