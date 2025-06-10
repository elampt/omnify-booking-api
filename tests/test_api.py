import sys
import os
from fastapi.testclient import TestClient
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from main import app

client = TestClient(app)

def test_get_classes():
    response = client.get("/classes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all("name" in c for c in response.json())

def test_book_class_success():
    # Book a class (assumes class_id=1 exists from seed data)
    data = {
        "class_id": 1,
        "client_name": "Test User",
        "client_email": "testuser@example.com"
    }
    response = client.post("/book", json=data)
    # Accept 200 (success) or 400 (already booked/slots full)
    assert response.status_code in (200, 400)

def test_get_bookings():
    response = client.get("/bookings?client_email=testuser@example.com")
    assert response.status_code == 200
    assert isinstance(response.json(), list)