import mysql.connector

# Configurar la conexión
config = {
    'host': 'localhost',
    'user': 'sistema_python',
    'password': '2025',
    'database': 'diagnosticos_db',
    'port': 3306,
}

# Crear conexión
try:
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        print("Conexión exitosa a MySQL")
        cursor = connection.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"Versión de MySQL: {version[0]}")
except mysql.connector.Error as e:
    print(f"Error conectando a MySQL: {e}")
finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión cerrada")
