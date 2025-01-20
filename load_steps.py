from behave import given
from app import app

@given("the product data is loaded")
def step_impl(context):
    context.client = app.test_client()
    for row in context.table:
        product = {
            "name": row["name"],
            "category": row["category"],
            "price": float(row["price"]),
            "availability": row["availability"] == "True"
        }
        context.client.post("/products", json=product)