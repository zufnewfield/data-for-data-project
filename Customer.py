#from functools import reduce
import random
#import pandas as pd
import names
from faker import Faker
from datetime import datetime, timedelta

FAKE = Faker()


def gen_Customer(n: int):
    r = range(1, n + 1)
    
    customerID = r
    c_kind = [random.choice(['R','S']) for _ in r]
    phoneNumber = [FAKE.phone_number().replace("\n", " ") for _ in r]
    email = [FAKE.ascii_company_email().replace("\n", " ") for _ in r]
    address =  [FAKE.address().replace("\n", " ") for _ in r]
    name = [FAKE.first_name().replace("\n", " ") for _ in r]
    
    coloms_name = ("customerID", "c_kind", "phoneNumber","email", "address", "name")
    t_name = "smarkovi.Customer"

    data = ""
    for i in r:
        data += f"insert into {t_name} ({', '.join(coloms_name)}) values ({customerID[i-1]}, '{c_kind[i-1]}', '{phoneNumber[i-1]}', '{email[i-1]}', '{address[i-1]}', '{name[i-1]}');\n"
    with open("gen_Customer.sql", "w") as f:
        f.write(data)


gen_Customer(400)