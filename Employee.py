#from functools import reduce
import random
#import pandas as pd
import names
from faker import Faker
from datetime import datetime, timedelta

FAKE = Faker()


def gen_Employee(n: int):
    r = range(1, n + 1)
    
    employeeID = r
    role = [random.choice(['cleaner','attendant','sec','seller']) for _ in r]
    phoneNumber = [FAKE.phone_number().replace("\n", " ") for _ in r]
    email = [FAKE.ascii_company_email().replace("\n", " ") for _ in r]
    address =  [FAKE.address().replace("\n", " ") for _ in r]
    startCareerDate = [str(datetime.now() + timedelta(days=random.randint(-50, 100), hours=random.randint(-100, 100)))[:-10].replace("-", "/") for _ in r]
    airportID = [random.randint(1,n+1) for _ in r]
    fullname = [FAKE.first_name().replace("\n", " ") for _ in r]
    coloms_name = ("employeeID", "role", "phoneNumber","email", "address", "startCareerDate", "airportID","fullname")
    t_name = "smarkovi.Employee"

    data = ""
    for i in r:
        data += f"insert into {t_name} ({', '.join(coloms_name)}) values ({employeeID[i-1]}, '{role[i-1]}', '{phoneNumber[i-1]}', '{email[i-1]}', '{address[i-1]}', to_date('{startCareerDate[i-1]}', 'YYYY/MM/DD HH24:MI'), {airportID[i-1]},'{fullname[i-1]}');\n"
    with open("gen_Employee.sql", "w") as f:
        f.write(data)


gen_Employee(400)