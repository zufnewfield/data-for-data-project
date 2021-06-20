#from functools import reduce
import random
#import pandas as pd
import names
from faker import Faker
from datetime import datetime, timedelta

FAKE = Faker()


def gen_FilghtTicket(n: int):
    r = range(1, n + 1)

    ticketID = r
    status  = [random.choice(['T','F']) for _ in r]
    flightID = [random.randint(1,n+1) for _ in r]
    seatID = [random.randint(1,n+1) for _ in r]
    price = [random.randint(1,n+1) for _ in r]
    customerID = [random.randint(1,n+1) for _ in r]

    coloms_name = ("ticketID", "status", "flightID","seatID", "price", "customerID")
    t_name = "smarkovi.FilghtTicket"

    data = ""
    for i in r:
        data += f"insert into {t_name} ({', '.join(coloms_name)}) values ({ticketID[i-1]}, '{status[i-1]}', {flightID[i-1]}, {seatID[i-1]}, {price[i-1]}, {customerID[i-1]});\n"
    with open("gen_FilghtTicket.sql", "w") as f:
        f.write(data)


gen_FilghtTicket(400)