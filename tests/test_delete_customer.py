from db_steps import db_steps


def test_delete_existing_customer(db_client, create_customer, cleanup_user):
    id = create_customer
    assert db_steps.delete_customer(db_client, id=id)
    cleanup_user(id)


def test_delete_not_existing_customer(db_client, generate_not_existing_customer_id):
    id = generate_not_existing_customer_id
    assert db_steps.delete_customer(db_client, id=id)