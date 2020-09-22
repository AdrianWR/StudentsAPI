import requests

guiga = {
          "name": "Guilhemar Caixeta",
          "intra_id": "guiga",
          "projects": [
            "cub3d"
          ]
        }

gus = {
          "name": "Gustavo Belfort",
          "intra_id": "gus",
          "projects": [
            "libft",
            "minirt"
          ]
        }

aroque = {
          "name": "Adrian Roque",
          "intra_id": "aroque"
         }

no_name = {
          "intra_id": "no_name",
          "projects": [
            "libft",
            "minirt"
          ]
        }

odd_data = {
            "cake": "banana",
            "juice": "orange"
          }

def post(url, dict, expected_value):
    response = requests.post("http://127.0.0.1:3000/students", json=dict)
    print(response.request.body)
    print(response.request.headers)
    assert response.status_code == expected_value
    assert response.headers['Content-Type'] == "application/json"

def test_post_students():
    post("http://127.0.0.1:3000/students", gus, 201)
    post("http://127.0.0.1:3000/students", guiga, 201)
    post("http://127.0.0.1:3000/students", aroque, 201)
    post("http://127.0.0.1:3000/students", gus, 401)
    post("http://127.0.0.1:3000/students", {}, 400)
    post("http://127.0.0.1:3000/students", no_name, 400)
    post("http://127.0.0.1:3000/students", odd_data, 400)
    post("http://127.0.0.1:3000/stu", gus, 401)
    post("http://127.0.0.1:3000", gus, 401)
