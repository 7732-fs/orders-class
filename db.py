import sqlite3

def setup(filename="orders.sqlite"):
    with sqlite3.connect(filename) as conn:
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS customers(id INTEGER PRIMARY KEY, customer_name TEXT, phone_number TEXT, discount TEXT)")
        conn.commit()
        cur.execute("CREATE TABLE IF NOT EXISTS orders(id INTEGER PRIMARY KEY, customer_id INT, license_number TEXT, date TEXT, wash_type TEXT, car_type TEXT, price TEXT, FOREIGN KEY (customer_id) REFERENCES customers(id))")
        conn.commit()

    
setup()