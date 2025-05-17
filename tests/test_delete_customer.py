import pytest
from db_steps import db_steps

def test_delete_existing_customer(db_client, get_existing_customer_from_db):
    id = get_existing_customer_from_db[0]
    assert db_steps.delete_customer(db_client, id=id)

def test_delete_not_existing_customer(db_client, get_existing_customer_from_db):
    assert not db_steps.delete_customer(db_client, id=45345353453)    # TODO: заменить на метод, который действительно получает не существующий id
