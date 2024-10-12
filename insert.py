import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None

def add_products(conn, products):
    """
    Insert many products at once
    :param conn: Connection object
    :param products: list of tuples (nazwa, category)
    :return:
    """
    sql = '''INSERT INTO products(nazwa, category)
             VALUES(?,?)'''
    cur = conn.cursor()
    cur.executemany(sql, products)  # Dodaj wiele produktów
    conn.commit()

def add_sales(conn, sales):
    """
    Insert many sales at once
    :param conn: Connection object
    :param sales: list of tuples (product_id, value, volume, opis, date)
    :return:
    """
    sql = '''INSERT INTO sales(product_id, value, volume, opis, date)
             VALUES(?,?,?,?,?)'''
    cur = conn.cursor()
    cur.executemany(sql, sales)  # Dodaj wiele sprzedaży
    conn.commit()

def add_sale(conn, sale):
    """
    Insert a single sale
    :param conn: Connection object
    :param sale: tuple (product_id, value, volume, opis, date)
    :return:
    """
    sql = '''INSERT INTO sales(product_id, value, volume, opis, date)
             VALUES(?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, sale)  # Dodaj pojedynczą sprzedaż
    conn.commit()

if __name__ == "__main__":
    # Lista produktów do dodania
    products = [
        ("chleb", "pieczywo"),
        ("mleko", "nabiał"),
        ("ser", "nabiał")
    ]

    # Użycie context managera dla połączenia z bazą danych
    db_file = "database.db"
    with sqlite3.connect(db_file) as conn:
        if conn is not None:
            # Dodaj produkty
            add_products(conn, products)

            # Pobierz ID produktów po dodaniu
            cur = conn.cursor()
            cur.execute("SELECT id FROM products")
            product_ids = cur.fetchall()

            # Przygotowanie danych sprzedaży z wykorzystaniem ID produktów
            sales = [
                (product_ids[0][0], 20, 4, "sklep nr 1", "2020-05-11 15:00:00"),
                (product_ids[1][0], 10, 2, "sklep nr 2", "2020-05-12 12:00:00"),
                (product_ids[2][0], 9, 3, "sklep nr 2", "2020-05-13 14:00:00"),
                (product_ids[2][0], 15, 3, "sklep nr 3", "2020-05-13 14:00:00")
            ]

            # Dodaj sprzedaż
            add_sales(conn, sales)

            # Dodaj pojedynczą sprzedaż
            single_sale = (product_ids[1][0], 25, 5, "sklep nr 4", "2020-05-14 09:00:00")
            add_sale(conn, single_sale)

            print("Produkty i sprzedaż zostały dodane.")
        else:
            print("Nie udało się połączyć z bazą danych.")
