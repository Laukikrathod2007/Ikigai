@echo off
echo ========================================
echo Mental Wellness Platform
echo ========================================
echo.
echo Starting Flask backend server...
echo.
cd backend
start "Flask Server" cmd /k "python app.py"
timeout /t 3 /nobreak >nul
echo.
echo Starting frontend server...
cd ..\frontend
start "Frontend Server" cmd /k "python -m http.server 8000"
timeout /t 2 /nobreak >nul
echo.
echo ========================================
echo Servers are starting!
echo ========================================
echo.
echo Frontend: http://localhost:8000/demo.html
echo Backend API: http://localhost:5000
echo.
echo Opening browser...
start http://localhost:8000/demo.html
echo.
echo Press any key to exit...
pause >nul
