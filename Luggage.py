
	
#from functools import reduce
import random
#import pandas as pd
import names
from faker import Faker
from datetime import datetime, timedelta

FAKE = Faker()


def gen_Luggage(n: int):
    r = range(1, n + 1)
    
    luggageID = r
    weight = [random.randint(1,n+1) for _ in r]
    ticketID = [random.randint(1,n+1) for _ in r]

    coloms_name = ("luggageID", "weight", "ticketID") 
    t_name = "smarkovi.Luggage"

    data = ""
    for i in r:
        data += f"insert into {t_name} ({', '.join(coloms_name)}) values ({luggageID[i-1]}, {weight[i-1]}, {ticketID[i-1]});\n"
    with open("gen_Luggage.sql", "w") as f:
        f.write(data)


gen_Luggage(400)	