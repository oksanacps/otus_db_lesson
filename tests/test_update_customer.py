from db_steps import db_steps
from datetime import datetime


def test_update_existing_customer(db_client, get_existing_customer_from_db):
    customer_data = {
        "firstname": "TestUpdated",
        "lastname": "TestUpdated",
        "email": "TestUpdated1@test.ru",
        "telephone": "+73456677888",
    }

    id = get_existing_customer_from_db[0]
    db_steps.update_customer_data(db_client, customer_data, id)
    customer_data = db_steps.get_customer_data_by_id(db_client, id)[0]
    assert customer_data[4] == "TestUpdated"
    assert customer_data[5] == "TestUpdated"
    assert customer_data[6] == "TestUpdated1@test.ru"
    assert customer_data[7] == "+73456677888"


def test_update_not_existing_customer(db_client, generate_not_existing_customer_id):
    customer_data = {
        "firstname": "TestUpdatedNotExist",
        "lastname": "TestUpdatedNotExist",
        "email": "TestUpdatedNotExist@test.ru",
        "telephone": "+76544325522",
    }

    id = generate_not_existing_customer_id
    db_steps.update_customer_data(db_client, customer_data, id)
    customer_data = db_steps.get_customer_data_by_id(db_client, id)
    assert len(customer_data) == 0
