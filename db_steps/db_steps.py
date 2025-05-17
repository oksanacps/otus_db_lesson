from client.database.maria_db.db_client import MariaDbClient


def create_customer(db_client: MariaDbClient, customer_data: dict):
    """
    Создает клиента в БД.
    Возвращает id созданного клиента.
    """

    sql_request = f"""
        INSERT INTO oc_customer
            (customer_group_id, 
            firstname, lastname, 
            email, 
            telephone, 
            password, 
            language_id, 
            custom_field, 
            ip, 
            status, 
            safe, 
            token, 
            code, 
            date_added)
        VALUES ('123',
                '{customer_data.get("firstname")}',
                '{customer_data.get("lastname")}',
                '{customer_data.get("email")}',
                '{customer_data.get("telephone")}',
                '{customer_data.get("password")}',
                '0',
                '0',
                '192.168.0.1',
                '0',
                '0',
                'asd',
                'asd',
                '{customer_data.get("date_added")}');
    """
    db_client.execute(sql_request)
    sql_select = "SELECT LAST_INSERT_ID();"
    result = db_client.execute(sql_select)
    return result[0][0]


def get_customer_data_by_id(db_client: MariaDbClient, id: int):
    """
    Запрашивает данные пользователя по id.
    Возвращает данные.
    """

    sql_request = f"""
    SELECT *
    FROM oc_customer
    WHERE customer_id = {id}
    """

    customer_data = db_client.execute(sql_request)

    return customer_data


def get_customers(db_client: MariaDbClient):
    """
    Запрашивает все данные из таблицы oc_customer.
    Возвращает данные по всем клиентам.
    """

    sql_request = """
    SELECT *
    FROM oc_customer
    """

    customers_data = db_client.execute(sql_request)

    return customers_data


def update_customer_data(db_client: MariaDbClient, customer_data: dict, id: int):
    """
    Обновляет данные по клиенту.
    """

    try:
        sql_request = f"""
            UPDATE oc_customer 
            SET firstname = '{customer_data.get("firstname")}',
                lastname = '{customer_data.get("lastname")}',
                email ='{customer_data.get("email")}',
                telephone ='{customer_data.get("telephone")}'
            WHERE customer_id = {id};
        """
        db_client.execute(sql_request)


    except Exception as e:
        raise e(f"Ошибка обновления клиента {id}: {e}")


def delete_customer(db_client: MariaDbClient, id: int):
    """
    Удаляет пользователя по ID.
    Возвращает True (БД кол-во затронутых строк не возвращает)
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
        raise e(f"Ошибка удаления клиента {id}: {e}")
