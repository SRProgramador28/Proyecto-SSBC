from database.manager import DatabaseManager

class DatabaseManagerSingleton:
    _instance = None

    @staticmethod
    def get_instance():
        if DatabaseManagerSingleton._instance is None:
            DatabaseManagerSingleton._instance = DatabaseManager(
                host="127.0.0.1",
                user="sistema_python",
                password="2025",
                database="diagnosticos_db",
                port=3306
            )
        return DatabaseManagerSingleton._instance

