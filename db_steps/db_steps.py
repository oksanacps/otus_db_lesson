from client.database.maria_db.db_client import MariaDbClient


def create_customer(db_client: MariaDbClient, customer_data: dict):
    """
    Создает клиента в БД.
    Возвращает id созданного клиента.
    """

    params = (
        '123',  # customer_group_id
        customer_data.get("firstname"),
        customer_data.get("lastname"),
        customer_data.get("email"),
        customer_data.get("telephone"),
        customer_data.get("password"),
        '0',    # language_id
        '0',    # custom_field
        '192.168.0.1',  # ip
        '0',    # status
        '0',    # safe
        'asd',  # token
        'asd',  # code
        customer_data.get("date_added")
    )

    sql_request = """
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
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    try:
        db_client.execute(sql_request, params)
        sql_select = "SELECT LAST_INSERT_ID();"
        result = db_client.execute(sql_select)
        return list(result[0].values())[0]

    except Exception as e:
        raise AssertionError(f"Ошибка создания клиента")
    

def get_customer_data_by_id(db_client: MariaDbClient, id: int):
    """
    Запрашивает данные пользователя по id.
    Возвращает данные.
    """

    params = (
        id
    )

    sql_request = """
    SELECT *
    FROM oc_customer
    WHERE customer_id = %s;
    """

    try:
        customer_data = db_client.execute(sql_request, params)
        if customer_data:
            return customer_data[0]
        else:
            return None

    except Exception as e:
        raise AssertionError(f"Ошибка получения клиента {id}: {e}")

    
def get_customers(db_client: MariaDbClient):
    """
    Запрашивает все данные из таблицы oc_customer.
    Возвращает данные по всем клиентам.
    """

    sql_request = """
    SELECT *
    FROM oc_customer;
    """

    try:
        customers_data = db_client.execute(sql_request)
        return customers_data

    except Exception as e:
        raise AssertionError(f"Ошибка получения информации в таблице oc_customer")


def update_customer_data(db_client: MariaDbClient, customer_data: dict, id: int):
    """
    Обновляет данные по клиенту.
    """
    params = (
        customer_data.get("firstname"),
        customer_data.get("lastname"),
        customer_data.get("email"),
        customer_data.get("telephone"),
        id
    )

    sql_request = """
            UPDATE oc_customer 
            SET firstname = %s,
                lastname = %s,
                email = %s,
                telephone = %s
            WHERE customer_id = %s;
        """

    try:
        db_client.execute(sql_request, params)
        return True

    except Exception as e:
        raise AssertionError(f"Ошибка обновления клиента {id}: {e}")


def delete_customer(db_client: MariaDbClient, id: int):
    """
    Удаляет пользователя по ID.
    Возвращает True (БД кол-во затронутых строк не возвращает)
    """
    params = (
        id
    )

    sql_request = """
        DELETE 
        FROM oc_customer 
        WHERE customer_id = %s;
        """
    
    try:
        db_client.execute(sql_request, params)
        return True

    except Exception as e:
        raise ArithmeticError(f"Ошибка удаления клиента {id}: {e}")
