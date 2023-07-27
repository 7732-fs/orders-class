from faker import Faker
fake = Faker('he_IL')
# fake = Faker()
import random 
from db import query_db, get_dicts, setup
import datetime

def create_fake_customers(num=40):
    for i in range(num):
        sql=f"""
        INSERT INTO customers (customer_name, phone_number, discount) VALUES
        ('{fake.name().replace("'", "")}', '{fake.phone_number()}', '{random.randint(0,12)}')
        """
        query_db(sql)

def create_fake_orders(num=20):
    for i in range(num):
        sql=f"""
        INSERT INTO orders (license_number, customer_id, date, wash_type, car_type, price, car_color, car_company) VALUES
        ('{random.randint(600000, 700000)}', '{random.randint(1, 40)}', '{datetime.datetime(year=2023, month=1, day=1, hour=random.randint(0, 23), minute=random.randint(0,59))}', '{random.choice(["חיצוני", "פנימי", "פוליש"])}', '{random.choice(["פרטי", "גיפ", "מסחרי"])}', '{random.randint(60, 120)}',  '{random.choice(["blue", "green", "red", "orange", "silver"])}',  '{random.choice(["טויוטה", "מאזדה", "יונדאי", "אאודי", "במוו"])}')
        """
        query_db(sql)

#setup()
#create_fake_customers()
create_fake_orders()


# def find_order(date):
#     for order in orders:
#         if order[3]==date:
#             print(order)

# customer=query_db("select * from customers where id='16'")

# print(customer)
