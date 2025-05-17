import pymysql
import logging


class MariaDbClient:
    def __init__(self, host: str, port: int, user: str, password: str, db: str):
        self.connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            db=db,
            password=password
        )

    def execute(self, sql_request: str):
        try:
            with self.connection.cursor() as cursor:    # Нужно ли закрывать курсор (в данном случае закроектся через конт.менеджер, или в тестах это избыточно?)
                cursor.execute(sql_request)
                self.connection.commit()
                raw_data = cursor.fetchall()
                logging.info(f"--------------------------------")
                logging.info(self.connection.get_host_info())
            logging.info(f"Executed SQL request: {sql_request}")
            logging.info(f"Raw data: {raw_data}")
            logging.info(f"--------------------------------")
            return raw_data 
        except Exception as e:
            logging.error(f"Error executing SQL request: {e}")
            self.connection.rollback()
            raise e

    def close(self):
        logging.info("Closing DB connection...")
        self.connection.close()










