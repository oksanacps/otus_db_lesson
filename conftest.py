from datetime import datetime
from faker import Faker
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
def create_customer(db_client, generate_customer_data):
    id = db_steps.create_customer(db_client, generate_customer_data)

    return id


@pytest.fixture()
def generate_not_existing_customer_id(db_client):
    customers_data = db_steps.get_customers(db_client)
    count = 5
    while count != 0:
        random_id = random.randint(100000, 999999)
        if random_id not in customers_data:
            return random_id
        count -= 1


@pytest.fixture()
def cleanup_user(request, db_client):
    """
    Фикстура для удаления пользователей после теста.
    """
    users_to_cleanup = []
    def cleanup_users():
        for id in users_to_cleanup:
            db_steps.delete_customer(db_client, id)
    request.addfinalizer(cleanup_users)
    
    def add_user_for_cleanup(id):
        users_to_cleanup.append(id)

    return add_user_for_cleanup


@pytest.fixture()
def generate_customer_data():
    """
    Фикстура для генерации случайных данных клиента с помощью Faker.
    Возвращает словарь с данными клиента.
    """
    fake = Faker()

    firstname = fake.first_name()
    lastname = fake.last_name()
    email = fake.email()
    telephone = fake.phone_number()
    password = fake.password()
    date_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    customer_data = {
        "firstname": firstname,
        "lastname": lastname,
        "email": email,
        "telephone": telephone,
        "password": password,
        "date_added": date_added
    }
    return customer_data