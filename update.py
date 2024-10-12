import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def update(conn, table, id, **kwargs):
    """
    Update a row in the specified table based on the provided id and keyword arguments
    :param conn: Connection object
    :param table: table name
    :param id: row id
    :param kwargs: column-value pairs to update
    """
    parameters = [f"{k} = ?" for k in kwargs]
    parameters = ", ".join(parameters)
    values = tuple(kwargs.values()) + (id, )

    sql = f''' UPDATE {table}
               SET {parameters}
               WHERE id = ?'''
    try:
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        print("OK")
    except sqlite3.OperationalError as e:
        print(e)

if __name__ == "__main__":
    db_file = "database.db"

    # Użycie context managera dla połączenia z bazą danych
    with sqlite3.connect(db_file) as conn:
        # Przykład aktualizacji w tabeli "products" i "sales"
        update(conn, "products", 1 , category="pieczywo wytrawne")
        update(conn, "sales", 3, value=9) 
