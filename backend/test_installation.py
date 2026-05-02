"""
Quick test script to verify installation
"""

def test_imports():
    """Test that all required packages can be imported"""
    try:
        import fastapi
        print("✅ FastAPI imported successfully")
        
        import uvicorn
        print("✅ Uvicorn imported successfully")
        
        import pydantic
        print("✅ Pydantic imported successfully")
        
        import httpx
        print("✅ HTTPX imported successfully")
        
        import aiohttp
        print("✅ Aiohttp imported successfully")
        
        print("\n🎉 All dependencies installed successfully!")
        print("\nYou can now run: python main.py")
        
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

if __name__ == "__main__":
    test_imports()

# Made with Bob
