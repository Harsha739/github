from app import app

def test_list_all_products(client):
    response = client.get("/products")
    assert response.status_code == 200

def test_create_product(client):
    response = client.post("/products", json={"name": "New Product", "category": "Electronics", "price": 49.99, "availability": True})
    assert response.status_code == 201

def test_update_product(client):
    response = client.put("/products/1", json={"name": "Updated Product"})
    assert response.status_code == 200

def test_delete_product(client):
    response = client.delete("/products/1")
    assert response.status_code == 204

def test_find_by_category(client):
    response = client.get("/products?category=Books")
    assert response.status_code == 200