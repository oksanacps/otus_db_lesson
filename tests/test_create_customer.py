import pytest
from db_steps import db_steps
from datetime import datetime

NUM_CLIENT = 3

@pytest.mark.parametrize(
    "count_customer",
    range(NUM_CLIENT)
)
def test_create_new_customer(db_client, count_customer, generate_customer_data, cleanup_user):
    id = db_steps.create_customer(db_client, generate_customer_data)
    customer_data_from_db = db_steps.get_customer_data_by_id(db_client, id)
    assert customer_data_from_db["firstname"] == generate_customer_data["firstname"]
    assert customer_data_from_db["lastname"] == generate_customer_data["lastname"]
    assert customer_data_from_db["email"] == generate_customer_data["email"]
    assert customer_data_from_db["telephone"] == generate_customer_data["telephone"]
    assert customer_data_from_db["password"] == generate_customer_data["password"]
    assert customer_data_from_db["date_added"].strftime('%Y-%m-%d %H:%M:%S') == generate_customer_data["date_added"]   
    cleanup_user(id)
