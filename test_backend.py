import requests
import json

def test_backend_connection():
    """Test if the FastAPI backend is running and responding"""
    try:
        # Test the health check endpoint
        response = requests.get('http://localhost:8080/')
        print(f"Health check status: {response.status_code}")
        print(f"Health check response: {response.json()}")
        
        # Test the predict endpoint with sample data
        test_data = {
            'nutrition_input': [500.0, 20.0, 5.0, 0.0, 400.0, 100.0, 10.0, 10.0, 10.0],
            'ingredients': [],
            'params': {'n_neighbors': 5, 'return_distance': False}
        }
        
        response = requests.post('http://localhost:8080/predict/', json=test_data)
        print(f"Predict endpoint status: {response.status_code}")
        
        if response.status_code == 200:
            print("Backend is working correctly!")
            result = response.json()
            if result.get('output'):
                print(f"Received {len(result['output'])} recommendations")
            else:
                print("No recommendations returned")
        else:
            print(f"Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to backend. Make sure it's running on http://localhost:8080")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_backend_connection()
