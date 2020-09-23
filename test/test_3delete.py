import requests


def delete(id, expected_value):
    """Helper function to teste DELETE HTTP requests"""
    response = requests.delete(f"http://127.0.0.1:3000/students/{id}")
    print(response.request.body)
    print(response.request.headers)
    assert response.status_code == expected_value
    assert response.headers['Content-Type'] == "application/json"

def test_delete_students():
    delete(1, 200)
    delete(2, 200)
    delete(3, 200)
    delete(4200, 404)
