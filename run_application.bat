@echo off
echo Starting Diet Recommendation System...
echo.

echo Starting FastAPI Backend...
start "FastAPI Backend" cmd /k "cd FastAPI_Backend && python -m uvicorn main:app --host 0.0.0.0 --port 8080"

echo Waiting for backend to start...
timeout /t 5 /nobreak > nul

echo Starting Streamlit Frontend...
start "Streamlit Frontend" cmd /k "cd Streamlit_Frontend && streamlit run Hello.py"

echo.
echo Both services are starting...
echo Backend will be available at: http://localhost:8080
echo Frontend will be available at: http://localhost:8501
echo.
echo Press any key to close this window...
pause > nul
