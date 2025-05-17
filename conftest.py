import random
import pytest
import logging

from client.database.maria_db.db_client import MariaDbClient
from db_steps import db_steps

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def pytest_addoption(parser):
    parser.addoption("--db-host", action="store", default="localhost")
    parser.addoption("--db-port", action="store", default=3306)
    parser.addoption("--db-user", action="store", default="bn_opencart")
    parser.addoption("--db-password", action="store", default="")
    parser.addoption("--db-name", action="store", default="bitnami_opencart")


@pytest.fixture(scope="session")
def db_client(request):
    db_client = MariaDbClient(
        host=request.config.getoption("--db-host"),
        port=request.config.getoption("--db-port"),
        user=request.config.getoption("--db-user"),
        password=request.config.getoption("--db-password"),
        db=request.config.getoption("--db-name"),
    )
    assert db_client.connection.open

    yield db_client

    db_client.close()


@pytest.fixture()
def get_existing_customer_from_db(db_client):
    customers_data = db_steps.get_customers(db_client)
    try:
        customer_data = customers_data[0]
        return customer_data

    except IndexError as e:
        raise e("Ошибка получения клиента. Таблица oc_customer пустая")


@pytest.fixture()
def generate_not_existing_customer_id(db_client):
    customers_data = db_steps.get_customers(db_client)
    count = 5
    while count != 0:
        random_id = random.randint(100000, 999999)
        if random_id not in customers_data:
            return random_id
        count -= 1
