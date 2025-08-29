@echo off
echo Installing Diet Recommendation System Dependencies...
echo.

echo Installing Frontend Dependencies...
cd Streamlit_Frontend
pip install -r requirements.txt
cd ..

echo.
echo Installing Backend Dependencies...
cd FastAPI_Backend
pip install -r requirements.txt
cd ..

echo.
echo All dependencies installed successfully!
echo.
echo To run the application:
echo 1. Start the backend: cd FastAPI_Backend && python -m uvicorn main:app --host 0.0.0.0 --port 8080
echo 2. Start the frontend: cd Streamlit_Frontend && streamlit run Hello.py
echo.
pause
