from behave import when, then

@when("I request all products")
def step_impl(context):
    context.response = context.client.get("/products")

@then("I should see a list of products")
def step_impl(context):
    assert context.response.status_code == 200
    assert len(context.response.json) > 0