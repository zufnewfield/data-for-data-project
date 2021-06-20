
	
#from functools import reduce
import random
#import pandas as pd
import names
from faker import Faker
from datetime import datetime, timedelta

FAKE = Faker()


def gen_Maintenance(n: int):
    r = range(1, n + 1)
   
    checkDateTime = [str(datetime.now() + timedelta(days=random.randint(-50, 100), hours=random.randint(-100, 100)))[:-10].replace("-", "/") for _ in r]
    employeeID = r
    hitchID = [random.randint(1,n+1) for _ in r]
    
    coloms_name = ("checkDateTime", "employeeID", "hitchID") 
    t_name = "smarkovi.Maintenance"

    data = ""
    for i in r:
        data += f"insert into {t_name} ({', '.join(coloms_name)}) values (to_date('{checkDateTime[i-1]}', 'YYYY/MM/DD HH24:MI'),{employeeID[i-1]},{hitchID[i-1]});\n"
    with open("gen_Maintenance.sql", "w") as f:
        f.write(data)


gen_Maintenance(400)	