import sqlite3
from sqlite3 import Error

# Tworzenie połączenia
def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except Error as e:
       print(e)
   return None

# Tworzenie tabel
def execute_sql(conn, sql):
   """ Execute SQL
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

if __name__ == "__main__":
   create_products_sql = """
   -- products table
   CREATE TABLE IF NOT EXISTS products (
      id integer PRIMARY KEY,
      nazwa text NOT NULL,
      category text NOT NULL
   );
   """

   create_sales_sql = """
   -- sales table
   CREATE TABLE IF NOT EXISTS sales (
      id integer PRIMARY KEY,
      product_id integer NOT NULL,
      value integer NOT NULL,
      volume integer NOT NULL,
      opis TEXT,
      date text NOT NULL,
      FOREIGN KEY (product_id) REFERENCES products (id)
   );
   """

   db_file = "database.db"

   # Użycie context managera do automatycznego zamykania połączenia
   with sqlite3.connect(db_file) as conn:
       if conn is not None:
           execute_sql(conn, create_products_sql)
           execute_sql(conn, create_sales_sql)
       else:
           print("Nie udało się nawiązać połączenia z bazą danych.")
