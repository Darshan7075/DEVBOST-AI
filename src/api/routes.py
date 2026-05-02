"""
API Routes for DevBoost AI
FastAPI router for repository analysis
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.prompt_generator import get_all_tasks, get_task_description
from services.bob_executor import execute_with_bob


class AnalyzeRequest(BaseModel):
    """Request model for analysis endpoint"""
    repo: str
    task: str
    level: Optional[str] = "basic"
    
    class Config:
        schema_extra = {
            "example": {
                "repo": "https://github.com/username/repo",
                "task": "explain",
                "level": "advanced"
            }
        }


router = APIRouter(prefix="/api/v1", tags=["analysis"])


@router.post("/analyze")
async def analyze(data: AnalyzeRequest):
    """
    Analyze a GitHub repository with enhanced prompts
    
    Args:
        data: Request containing repo URL, task type, and enhancement level
        
    Returns:
        Analysis result with enhanced prompt and IBM Bob response
        
    Raises:
        HTTPException: If task type or enhancement level is invalid
    """
    repo = data.repo
    task = data.task
    level = data.level
    
    # Validate task type
    valid_tasks = get_all_tasks()
    if task not in valid_tasks:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid task. Must be one of: {', '.join(valid_tasks)}"
        )
    
    # Validate enhancement level
    valid_levels = ["basic", "advanced", "detailed"]
    if level not in valid_levels:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid level. Must be one of: {', '.join(valid_levels)}"
        )
    
    # Execute with Bob using enhanced prompts
    result = execute_with_bob(repo, task, level)
    
    return result


@router.get("/tasks")
async def get_tasks():
    """
    Get list of available analysis tasks
    
    Returns:
        List of task types with descriptions
    """
    tasks = get_all_tasks()
    return {
        "tasks": [
            {
                "name": task,
                "description": get_task_description(task)
            }
            for task in tasks
        ]
    }


@router.get("/health")
async def health_check():
    """
    Health check endpoint
    
    Returns:
        Service status
    """
    return {
        "status": "healthy",
        "service": "DevBoost AI API",
        "version": "1.0.0"
    }

# Made with Bob
