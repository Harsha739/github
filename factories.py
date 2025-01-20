from faker import Faker
import random

fake = Faker()

def create_fake_product():
    """Generate a fake product dictionary"""
    return {
        "id": fake.uuid4(),
        "name": fake.word(),
        "category": random.choice(["Electronics", "Clothing", "Books"]),
        "price": round(random.uniform(10.0, 100.0), 2),
        "availability": random.choice([True, False])
    }

if _name_ == "_main_":
    # Example to generate 5 fake products
    products = [create_fake_product() for _ in range(5)]
    print(products)