from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Chatbot API"}

def test_chat_endpoint():
    response = client.post("/chat", json={"query": "What is the weather today?"})
    assert response.status_code == 200
    assert "bot_message" in response.json()

def test_action_endpoint():
    response = client.post("/action", json={"action_type": "create_order", "parameters": {"order_id": "12345"}})
    assert response.status_code == 200
    assert "bot_message" in response.json()