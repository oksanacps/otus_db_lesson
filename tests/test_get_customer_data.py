from db_steps import db_steps


def test_get_customer_data(db_client, create_customer, cleanup_user):
    id = create_customer
    customer_data = db_steps.get_customer_data_by_id(db_client, id=id)
    assert len(customer_data) > 0
    cleanup_user(id)
