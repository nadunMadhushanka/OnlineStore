def test_create_item(client):
    payload = {"name": "Bell Pepper", "price": 450.0}
    response = client.post("/api/v1/items", json=payload)
    assert response.status_code == 201
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Bell Pepper"
    
def test_read_existing_item(client):
    response = client.get("/api/v1/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Bell Pepper"

def test_read_non_existing_item(client):
    response = client.get("/api/v1/items/99")
    assert response.status_code == 404