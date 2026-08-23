from fastapi.testclient import TestClient
from main import app

client=TestClient(app)

# Test Home API
def test_home():
    response=client.get("/")
    # Status code check
    assert response.status_code == 200
    # Response Data check
    assert response.json() == {"message":"Hello, Akhil..!"}

# Test Add api
def test_add_response():
    response=client.get("/add?a=5&b=10")
    assert response.status_code == 200
    assert response.json() == 15