import pandas as pd
from random import choice
from numpy.random import normal
from fastapi import FastAPI


names = ["Alice","Olivia","Elizabeth","Emily","Alex", "Bob", "Liam", "David"]


app = FastAPI()


@app.get('/')
def get_random(n = 10000):
    data_name = [choice(names) for i in range(n)]
    data_height = normal(180, 7, n)
    
    data = pd.DataFrame(list(zip(data_name, data_height)),
              columns=['name','height[cm]'])

    return data
