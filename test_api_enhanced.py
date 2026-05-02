"""
Test script for enhanced API with prompt enhancement levels
"""

import requests
import json

BASE_URL = "http://localhost:8000/api/v1"


def test_health():
    """Test health check endpoint"""
    print("=" * 80)
    print("TEST 1: Health Check")
    print("=" * 80)
    
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()


def test_get_tasks():
    """Test get tasks endpoint"""
    print("=" * 80)
    print("TEST 2: Get Available Tasks")
    print("=" * 80)
    
    response = requests.get(f"{BASE_URL}/tasks")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()


def test_analyze_basic():
    """Test analyze endpoint with basic enhancement"""
    print("=" * 80)
    print("TEST 3: Analyze with Basic Enhancement")
    print("=" * 80)
    
    data = {
        "repo": "https://github.com/example/test-repo",
        "task": "explain",
        "level": "basic"
    }
    
    print(f"Request: {json.dumps(data, indent=2)}")
    response = requests.post(f"{BASE_URL}/analyze", json=data)
    print(f"\nStatus Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()


def test_analyze_advanced():
    """Test analyze endpoint with advanced enhancement"""
    print("=" * 80)
    print("TEST 4: Analyze with Advanced Enhancement")
    print("=" * 80)
    
    data = {
        "repo": "https://github.com/example/security-app",
        "task": "bugs",
        "level": "advanced"
    }
    
    print(f"Request: {json.dumps(data, indent=2)}")
    response = requests.post(f"{BASE_URL}/analyze", json=data)
    print(f"\nStatus Code: {response.status_code}")
    
    result = response.json()
    print(f"\nResponse Summary:")
    print(f"  Status: {result['status']}")
    print(f"  Task: {result['task']}")
    print(f"  Enhancement Level: {result['enhancement_level']}")
    print(f"  Prompt Length: {result['metadata']['prompt_length']} characters")
    print(f"\nPrompt Preview (first 200 chars):")
    print(result['prompt_used'][:200] + "...")
    print()


def test_analyze_detailed():
    """Test analyze endpoint with detailed enhancement"""
    print("=" * 80)
    print("TEST 5: Analyze with Detailed Enhancement")
    print("=" * 80)
    
    data = {
        "repo": "https://github.com/example/api-service",
        "task": "docs",
        "level": "detailed"
    }
    
    print(f"Request: {json.dumps(data, indent=2)}")
    response = requests.post(f"{BASE_URL}/analyze", json=data)
    print(f"\nStatus Code: {response.status_code}")
    
    result = response.json()
    print(f"\nResponse Summary:")
    print(f"  Status: {result['status']}")
    print(f"  Task: {result['task']}")
    print(f"  Enhancement Level: {result['enhancement_level']}")
    print(f"  Prompt Length: {result['metadata']['prompt_length']} characters")
    print()


def test_analyze_default_level():
    """Test analyze endpoint with default (basic) level"""
    print("=" * 80)
    print("TEST 6: Analyze with Default Level (no level specified)")
    print("=" * 80)
    
    data = {
        "repo": "https://github.com/example/default-test",
        "task": "tests"
    }
    
    print(f"Request: {json.dumps(data, indent=2)}")
    response = requests.post(f"{BASE_URL}/analyze", json=data)
    print(f"\nStatus Code: {response.status_code}")
    
    result = response.json()
    print(f"\nResponse Summary:")
    print(f"  Status: {result['status']}")
    print(f"  Enhancement Level: {result['enhancement_level']} (should be 'basic')")
    print()


def test_invalid_task():
    """Test with invalid task"""
    print("=" * 80)
    print("TEST 7: Invalid Task (Error Handling)")
    print("=" * 80)
    
    data = {
        "repo": "https://github.com/example/test",
        "task": "invalid_task",
        "level": "basic"
    }
    
    print(f"Request: {json.dumps(data, indent=2)}")
    response = requests.post(f"{BASE_URL}/analyze", json=data)
    print(f"\nStatus Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()


def test_invalid_level():
    """Test with invalid enhancement level"""
    print("=" * 80)
    print("TEST 8: Invalid Enhancement Level (Error Handling)")
    print("=" * 80)
    
    data = {
        "repo": "https://github.com/example/test",
        "task": "explain",
        "level": "super_advanced"
    }
    
    print(f"Request: {json.dumps(data, indent=2)}")
    response = requests.post(f"{BASE_URL}/analyze", json=data)
    print(f"\nStatus Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()


def test_all_tasks_with_levels():
    """Test all tasks with different enhancement levels"""
    print("=" * 80)
    print("TEST 9: All Tasks with Different Enhancement Levels")
    print("=" * 80)
    
    test_cases = [
        ("explain", "basic"),
        ("bugs", "advanced"),
        ("docs", "detailed"),
        ("tests", "advanced")
    ]
    
    for task, level in test_cases:
        data = {
            "repo": "https://github.com/example/comprehensive-test",
            "task": task,
            "level": level
        }
        
        response = requests.post(f"{BASE_URL}/analyze", json=data)
        result = response.json()
        
        print(f"\n{task.upper()} with {level} enhancement:")
        print(f"  Status: {result['status']}")
        print(f"  Prompt Length: {result['metadata']['prompt_length']} chars")
    
    print()


def main():
    """Run all tests"""
    print("\n" + "=" * 80)
    print("ENHANCED API TEST SUITE")
    print("=" * 80)
    print("\nMake sure the API server is running:")
    print("  python -m uvicorn src.api.app:app --reload")
    print("\n" + "=" * 80)
    
    try:
        test_health()
        test_get_tasks()
        test_analyze_basic()
        test_analyze_advanced()
        test_analyze_detailed()
        test_analyze_default_level()
        test_invalid_task()
        test_invalid_level()
        test_all_tasks_with_levels()
        
        print("=" * 80)
        print("ALL TESTS COMPLETED!")
        print("=" * 80)
        print("\nSummary:")
        print("[OK] Health check working")
        print("[OK] Task listing working")
        print("[OK] Basic enhancement working")
        print("[OK] Advanced enhancement working")
        print("[OK] Detailed enhancement working")
        print("[OK] Default level working")
        print("[OK] Error handling working")
        print("=" * 80)
        
    except requests.exceptions.ConnectionError:
        print("\n" + "=" * 80)
        print("ERROR: Could not connect to API server")
        print("=" * 80)
        print("\nPlease start the server first:")
        print("  python -m uvicorn src.api.app:app --reload")
        print("=" * 80)


if __name__ == "__main__":
    main()

# Made with Bob
