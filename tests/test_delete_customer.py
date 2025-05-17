from db_steps import db_steps


def test_delete_existing_customer(db_client, get_existing_customer_from_db):
    id = get_existing_customer_from_db[0]
    assert db_steps.delete_customer(db_client, id=id)


def test_delete_not_existing_customer(db_client, generate_not_existing_customer_id):
    id = generate_not_existing_customer_id
    assert db_steps.delete_customer(db_client, id=id)
