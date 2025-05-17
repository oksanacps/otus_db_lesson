from db_steps import db_steps


def test_get_customer_data(db_client, get_existing_customer_from_db):
    id = get_existing_customer_from_db[0]
    customer_data = db_steps.get_customer_data_by_id(db_client, id=id)
    assert len(customer_data) > 0
