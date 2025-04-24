from ..core.database.manager import DatabaseManager

db = DatabaseManager(host="localhost", user="sistema_python", password="2025", 
                     database="diagnosticos_db", port=3306)

db.connect()
if not db.connection:
    print("No se pudo conectar a la base de datos.")
    exit(1)
db.init_schema()

query = """
    SELECT 
        table_name AS nombre, 
        table_type AS tipo
    FROM 
        information_schema.tables 
    WHERE 
        table_schema = %s
    ORDER BY 
        table_type, table_name
    """

rc = db.execute_query(query, (db.database,))
if rc:
        print(f"\n{'NOMBRE':<30}{'TIPO':<15}")
        print("-" * 45)
        for nombre, tipo_r in rc:
            tipo = "Vista" if tipo_r == 'VIEW' else "Tabla"
            print(f"{nombre:<30}{tipo:<15}")

db.close()
