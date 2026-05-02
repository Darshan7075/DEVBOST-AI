@echo off
color 0B
echo ===================================================
echo     🚀 DEVBOST AI - AUTO GITHUB DEPLOY SCRIPT 🚀
echo ===================================================
echo.
echo Checking git status...
git status -s

echo.
echo Step 1: Adding all new changes...
git add .

echo.
set /p msg="Step 2: Enter your commit message (or press Enter for 'Auto update'): "
if "%msg%"=="" set msg=Auto update from DevBoost AI

echo.
echo Committing changes with message: "%msg%"
git commit -m "%msg%"

echo.
echo Step 3: Pushing code to GitHub...
git push

echo.
echo ===================================================
echo  ✅ DONE! Code uploaded successfully.
echo  Vercel and Render will now automatically deploy it!
echo ===================================================
pause
