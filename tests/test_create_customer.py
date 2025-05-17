import pytest
from db_steps import db_steps
from datetime import datetime


customer_data = {
    "user_1": {
        "firstname": "Test1",
        "lastname": "Test1",
        "email": "Test1@test.ru",
        "telephone": "+79993338871",
        "password": "123456781",
        "date_added": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    },
    "user_2": {
        "firstname": "Test2",
        "lastname": "Test2",
        "email": "Test2@test.ru",
        "telephone": "+79993338872",
        "password": "123456782",
        "date_added": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    },
    "user_3": {
        "firstname": "Test3",
        "lastname": "Test3",
        "email": "Test3@test.ru",
        "telephone": "+79993338873",
        "password": "123456783",
        "date_added": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    },
}


@pytest.mark.parametrize(
    "customer_data",
    [customer_data["user_1"], customer_data["user_2"], customer_data["user_3"]],
)
def test_create_new_customer(db_client, customer_data):
    id = db_steps.create_customer(db_client, customer_data)
    customer_data = db_steps.get_customer_data_by_id(db_client, id)
    assert len(customer_data) > 0
