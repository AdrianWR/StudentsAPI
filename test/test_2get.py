import requests

def get(url, expected_value):
    response = requests.get(url)
    print(response.request.body)
    print(response.request.headers)
    assert response.status_code == expected_value
    assert response.headers['Content-Type'] == "application/json"

def test_home():
    """Test HTTP status code for home API URL"""
    get("http://127.0.0.1:3000", 200)

def test_get_students():
    """Test and assert HTTP status code for GET requests"""
    get("http://127.0.0.1:3000/students", 200)
    get("http://127.0.0.1:3000/students?projects=libft", 200)
    get("http://127.0.0.1:3000/stu", 404)
