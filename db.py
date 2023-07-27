import sqlite3

def setup(filename="orders.sqlite"):
    with sqlite3.connect(filename) as conn:
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS customers(id INTEGER PRIMARY KEY, customer_name TEXT, phone_number TEXT, discount TEXT)")
        conn.commit()
        cur.execute("CREATE TABLE IF NOT EXISTS orders(id INTEGER PRIMARY KEY, customer_id INT, license_number TEXT, date TEXT, wash_type TEXT, car_type TEXT, price TEXT, car_color TEXT, car_company TEXT, FOREIGN KEY (customer_id) REFERENCES customers(id))")
        conn.commit()

def query_db(sql, filename="orders.sqlite"):
     with sqlite3.connect(filename) as conn:
        cur=conn.cursor()
        cur.execute(sql)
        conn.commit()
        return cur.fetchall()

def get_dicts(sql="SELECT * FROM orders"):
    orders=query_db(sql)
    keys=["id", "customer_id", "license_number", "date", "wash_type", "car_type", "price", "car_color", "car_company"]
    dicts_list=[]
    for order in orders:
        values=list(order)
        dict_row=dict(zip(keys, values))
        dicts_list.append(dict_row)
    return dicts_list

def get_companies():
    return get_dicts("SELECT DISTINCT car_company FROM orders")

#setup()
# orders=query_db("select * from orders")
