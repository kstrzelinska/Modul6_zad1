import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file"""
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None

def select_all(conn, table):
    """
    Query all rows in the table
    :param conn: the Connection object
    :param table: table name
    :return: rows fetched from the table
    """
    cur = conn.cursor()
    try:
        cur.execute(f"SELECT * FROM {table}")
        rows = cur.fetchall()
        return rows
    except sqlite3.Error as e:
        print(e)
        return []

def select_where(conn, table, **query):
    """
    Query rows from table with conditions from **query dict
    :param conn: the Connection object
    :param table: table name
    :param query: dict of attributes and values
    :return: rows fetched from the table
    """
    cur = conn.cursor()
    try:
        qs = []
        values = ()
        for k, v in query.items():
            qs.append(f"{k}=?")
            values += (v,)
        q = " AND ".join(qs)
        sql = f"SELECT * FROM {table} WHERE {q}"
        cur.execute(sql, values)
        rows = cur.fetchall()
        return rows
    except sqlite3.Error as e:
        print(e)
        return []

if __name__ == "__main__":
    db_file = "database.db"

    # Użycie context managera dla połączenia z bazą danych
    with sqlite3.connect(db_file) as conn:
        # Pokaż wszystkie produkty
        products = select_all(conn, "products")
        print("Produkty:", products)

        # Pokaż wszystkie sprzedaże
        sales = select_all(conn, "sales")
        print("Sprzedaż:", sales)

        # Pokaż sprzedaż dla produktu o ID 1
        sales_for_product_1 = select_where(conn, "sales", product_id=1)
        print("Sprzedaż dla produktu 1:", sales_for_product_1)

    # Po zakończeniu bloku 'with' połączenie zostanie automatycznie zamknięte
