import mysql.connector
from mysql.connector import Error

class DatabaseManager:
    def __init__(self, host, user, password, database, port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.connection = None
        self.connect()

    def init_schema(self):
        try:
            with open("src/core/database/schema.sql", "r") as file:
                sql_commands = file.read().split(";")

                for command in sql_commands:
                    if command.strip():
                        self.execute_query(command.strip())

                print("Schema inicializado correctamente")
        except Error as e:
            print(f"Error al inicializar el esquema: {e}")
        except FileNotFoundError:
            print("El archivo schema.sql no se encontró")

    def connect(self):
        if self.connection and self.connection.is_connected():
            return
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexión exitosa")
        except Error as e:
            print(f"Error al conectar: {e}")
            self.connection = None

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

    def execute_query(self, query, params=None, fetch="all"):
        if not self.connection or not self.connection.is_connected():
            self.connect()

        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params) if params else cursor.execute(query)

            if query.strip().upper().startswith("SELECT"):
                if fetch == "one":
                    result = cursor.fetchone()
                else:
                    result = cursor.fetchall()
                return result
            else:
                self.connection.commit()
                return cursor.rowcount
        except Error as e:
            print(f"Error en consulta SQL: {e}")
            return None
        finally:
            cursor.close()
