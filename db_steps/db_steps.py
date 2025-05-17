import logging
from client.database.maria_db.db_client import MariaDbClient

def create_customer(db_client: MariaDbClient, customer_data: dict):
    pass

def get_customer_data_by_id(db_client: MariaDbClient, id: int):
    """
    Запрашивает данные пользователя по ID.
    Возвращает данные.
    """
    sql_request = f"""
    SELECT *
    FROM oc_customer
    WHERE customer_id = {id}"""

    customer_data = db_client.execute(sql_request)

    return customer_data

def get_customers(db_client: MariaDbClient):
    """
    Запрашивает данные из таблицы oc_customer.
    Возвращает данные по всем клиентам.
    """
    sql_request = """
    SELECT *
    FROM oc_customer
    """

    customers_data = db_client.execute(sql_request)

    return customers_data

def update_customer_data(db_client: MariaDbClient, customer_data: dict, id: int):
    pass

def delete_customer(db_client: MariaDbClient, id: int):
    """
    Удаляет пользователя по ID.
    Возвращает True, если пользователь был удалён, False если не найден.
    """
    try:
        sql_request = f"""
        DELETE 
        FROM oc_customer 
        WHERE customer_id = {id}
        """
        db_client.execute(sql_request)
        
        return True
        
    except Exception as e:
        logging.error(f"Error deleting user {id}: {e}")
        raise