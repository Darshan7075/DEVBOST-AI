"""
Analyze Routes - API endpoints for repository analysis
Handles POST /analyze requests with IBM Bob integration
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, validator
from typing import Optional
import re

from services.bob_integration import analyze_with_bob

# Create router
router = APIRouter(tags=["analysis"])


class AnalyzeRequest(BaseModel):
    """Request model for repository analysis"""
    repo_url: str = Field(
        ...,
        description="GitHub repository URL",
        example="https://github.com/username/repository"
    )
    task: str = Field(
        ...,
        description="Analysis task type",
        example="explain"
    )
    
    @validator('repo_url')
    def validate_repo_url(cls, v):
        """Validate GitHub repository URL format"""
        if not v or not v.strip():
            raise ValueError("Repository URL cannot be empty")
        
        # Basic GitHub URL validation
        github_pattern = r'^https?://github\.com/[\w-]+/[\w.-]+/?$'
        if not re.match(github_pattern, v.strip()):
            raise ValueError(
                "Invalid GitHub URL format. Expected: https://github.com/username/repository"
            )
        
        return v.strip()
    
    @validator('task')
    def validate_task(cls, v):
        """Validate task type"""
        valid_tasks = ['explain', 'docs', 'bugs', 'tests']
        if v not in valid_tasks:
            raise ValueError(
                f"Invalid task. Must be one of: {', '.join(valid_tasks)}"
            )
        return v
    
    class Config:
        schema_extra = {
            "example": {
                "repo_url": "https://github.com/username/repository",
                "task": "explain"
            }
        }


class AnalyzeResponse(BaseModel):
    """Response model for analysis results"""
    status: str
    task: str
    repo_url: str
    result: dict


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_repository(request: AnalyzeRequest):
    """
    Analyze a GitHub repository using IBM Bob
    
    This endpoint processes a GitHub repository URL and performs
    the requested analysis task using IBM Bob's AI capabilities.
    
    **Supported Tasks:**
    - `explain`: Explains the project purpose, architecture, and workflow
    - `docs`: Generates comprehensive documentation
    - `bugs`: Identifies bugs, security issues, and bad practices
    - `tests`: Generates unit test cases with edge cases
    
    **Args:**
    - repo_url: Valid GitHub repository URL
    - task: Type of analysis to perform
    
    **Returns:**
    - Analysis results with structured output from IBM Bob
    
    **Raises:**
    - 400: Invalid input (bad URL or task type)
    - 500: Analysis failed or internal error
    """
    try:
        # Call IBM Bob integration service
        result = await analyze_with_bob(
            repo_url=request.repo_url,
            task=request.task
        )
        
        return AnalyzeResponse(
            status="success",
            task=request.task,
            repo_url=request.repo_url,
            result=result
        )
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Analysis failed: {str(e)}"
        )


@router.get("/tasks")
async def get_available_tasks():
    """
    Get list of available analysis tasks
    
    Returns information about all supported analysis tasks
    including their descriptions and use cases.
    """
    return {
        "tasks": [
            {
                "name": "explain",
                "description": "Explains the project purpose, architecture, and workflow",
                "use_case": "Understanding a new codebase"
            },
            {
                "name": "docs",
                "description": "Generates comprehensive documentation including README",
                "use_case": "Creating project documentation"
            },
            {
                "name": "bugs",
                "description": "Identifies bugs, security issues, and bad practices",
                "use_case": "Code review and quality assurance"
            },
            {
                "name": "tests",
                "description": "Generates unit test cases with edge cases",
                "use_case": "Improving test coverage"
            }
        ]
    }

# Made with Bob
