import sqlite3
from sqlite3 import Error

def delete_where(conn, table, **kwargs):
    """
    Delete from table where attributes match the given conditions
    :param conn: Connection to the SQLite database
    :param table: table name
    :param kwargs: dict of attributes and values
    :return:
    """
    qs = []
    values = tuple()
    for k, v in kwargs.items():
        qs.append(f"{k}=?")
        values += (v,)
    q = " AND ".join(qs)

    sql = f'DELETE FROM {table} WHERE {q}'
    try:
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        print("Deleted")
    except sqlite3.Error as e:
        print(f"Error: {e}")

def delete_all(conn, table):
    """
    Delete all rows from the table
    :param conn: Connection to the SQLite database
    :param table: table name
    :return:
    """
    sql = f'DELETE FROM {table}'
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Deleted all rows")
    except sqlite3.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    db_file = "database.db"

    # Using a context manager for database operations
    with sqlite3.connect(db_file) as conn:
        # Delete specific record from 'sales'
        delete_where(conn, "sales", id=2)

        # Delete all records from 'products'
        delete_all(conn, "products")
