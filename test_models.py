import pytest
from models import Product  # Assuming a Product model exists

@pytest.fixture
def test_product():
    return Product(name="Test Product", category="Books", price=19.99, availability=True)

def test_create_product(test_product):
    assert test_product.name == "Test Product"
    assert test_product.category == "Books"

def test_find_by_name(session):
    product = Product.find_by_name("Test Product")
    assert product is not None

def test_update_product(session):
    product = Product.find_by_name("Test Product")
    product.name = "Updated Product"
    session.commit()
    updated_product = Product.find_by_name("Updated Product")
    assert updated_product.name == "Updated Product"

def test_delete_product(session):
    product = Product.find_by_name("Test Product")
    session.delete(product)
    session.commit()
    assert Product.find_by_name("Test Product") is None