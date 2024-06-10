import mysql.connector
from mysql.connector import Error

try:
  conn = mysql.connector.connect(
    host = "localhost",
    port= "10000",
    user = "admin",
    password="admin",
    db = "users"
  )

  if conn.is_connected():
    print("Conexion establecida.")
    info = conn.get_server_info()
    
except Error as er:
  print("Conexion no establecida", er)
finally:
  if conn.is_connected():
    conn.close()
    print("La conexion ha sido cerrada")