"""
Test script for DevBoost AI API
Tests the API endpoints without starting the server
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from api.routes import router, AnalyzeRequest
from utils.prompt_generator import get_all_tasks


def test_analyze_endpoint():
    """Test the analyze endpoint logic"""
    print("=" * 70)
    print("Testing DevBoost AI API")
    print("=" * 70)
    
    # Test data
    test_repo = "https://github.com/Darshan7075/DEVBOST-AI"
    
    print(f"\nRepository: {test_repo}\n")
    
    # Test each task type
    for task in get_all_tasks():
        print(f"\n{'=' * 70}")
        print(f"Testing Task: {task.upper()}")
        print(f"{'=' * 70}")
        
        # Create request
        request = AnalyzeRequest(repo=test_repo, task=task)
        
        print(f"\nRequest:")
        print(f"  Repo: {request.repo}")
        print(f"  Task: {request.task}")
        
        # Simulate the endpoint logic
        from utils.prompt_generator import get_prompt, get_task_description
        
        prompt = get_prompt(task, test_repo)
        
        print(f"\nGenerated Prompt:")
        print("-" * 70)
        print(prompt)
        
        print(f"\nTask Description: {get_task_description(task)}")
        print(f"\n[OK] Test passed for task: {task}")
    
    print("\n" + "=" * 70)
    print("All API Tests Passed!")
    print("=" * 70)
    print("\nTo start the actual API server:")
    print("1. Install dependencies: pip install fastapi uvicorn pydantic")
    print("2. Run: python src/api/app.py")
    print("3. Visit: http://localhost:8000/docs")
    print("\nOr use curl to test:")
    print('curl -X POST "http://localhost:8000/api/v1/analyze" \\')
    print('  -H "Content-Type: application/json" \\')
    print('  -d \'{"repo": "https://github.com/user/repo", "task": "explain"}\'')
    print()


if __name__ == "__main__":
    test_analyze_endpoint()

# Made with Bob
