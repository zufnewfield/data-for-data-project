#from functools import reduce
import random
#import pandas as pd
import names
from faker import Faker
from datetime import datetime, timedelta

FAKE = Faker()


def gen_hitch(n: int):
    r = range(1, n + 1)
    
    hitchID = r
    h_kind = [ chr(random.randint(65,90))  for _ in r]
    status  = [random.choice(['T','F']) for _ in r]
    description = [FAKE.text().replace("\n", " ") for _ in r]
    h_date = [str(datetime.now() + timedelta(days=random.randint(-50, 100), hours=random.randint(-100, 100)))[:-10].replace("-", "/") for _ in r]
    planeID = [random.randint(1,n+1) for _ in r]

    coloms_name = ("hitchID", "h_kind", "status","description", "h_date", "planeID")
    t_name = "smarkovi.hitch"

    data = ""
    for i in r:
        data += f"insert into {t_name} ({', '.join(coloms_name)}) values ({hitchID[i-1]}, '{h_kind[i-1]}', '{status[i-1]}', '{description[i-1]}', to_date('{h_date[i-1]}', 'YYYY/MM/DD HH24:MI'), {planeID[i-1]});\n"
    with open("gen_hitch.sql", "w") as f:
        f.write(data)


gen_hitch(400)