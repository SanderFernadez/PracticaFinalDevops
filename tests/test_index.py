import requests

def test_index_page():
    response = requests.get("http://localhost:9090")
    assert response.status_code == 200
    assert "Hola Mundo" in response.text
