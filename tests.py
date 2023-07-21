from faker import Faker
# fake = Faker('he_IL')
fake = Faker()
import random 
from db import query_db

def create_fake_data(num=40):
    # use query_db and SQL INSERT בשביל ליצור לקוחות 40
    for i in range(num):
        sql=f"""
        INSERT INTO customers (customer_name, phone_number, discount) VALUES
        ('{fake.name()}', '{fake.phone_number()}', '{random.randint(0,12)}')
        """
        query_db(sql)

create_fake_data()