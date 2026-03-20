from src.main.app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_deploy():
    client = app.test_client()
    response = client.get("/api/deploy")
    data = response.get_json()

    assert response.status_code == 200
    assert isinstance(data, dict)
    assert "node1" in data