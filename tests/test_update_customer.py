from db_steps import db_steps
from datetime import datetime


def test_update_existing_customer(db_client, create_customer, generate_customer_data, cleanup_user):
    id = create_customer
    db_steps.update_customer_data(db_client, generate_customer_data, id)
    customer_data = db_steps.get_customer_data_by_id(db_client, id)
    assert customer_data["firstname"] == generate_customer_data["firstname"]
    assert customer_data["lastname"] == generate_customer_data["lastname"]
    assert customer_data["email"] == generate_customer_data["email"] 
    assert customer_data["telephone"] == generate_customer_data["telephone"]
    cleanup_user(id)

def test_update_not_existing_customer(db_client, generate_not_existing_customer_id, generate_customer_data, cleanup_user):
    id = generate_not_existing_customer_id
    assert db_steps.update_customer_data(db_client, generate_customer_data, id)
    assert db_steps.get_customer_data_by_id(db_client, id) is None
    cleanup_user(id)