@echo off
echo ======================================================================
echo DevBoost AI - Backend Server Startup
echo ======================================================================
echo.

REM Check if virtual environment is activated
if not defined VIRTUAL_ENV (
    echo WARNING: Virtual environment not activated!
    echo Please run: venv\Scripts\activate
    echo.
    pause
    exit /b 1
)

echo Starting DevBoost AI Backend...
echo.

python start.py

pause

@REM Made with Bob
