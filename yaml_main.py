from data_auditing import *
import pandas as pd
import yaml
import random


with open(r"new.yaml") as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    # print(data['Name_of_students'])


# func_call = eval(data[0][0])
# print(func_call(df))

# print(type(data))
# print(data[0][0])
for key in data:
    df = pd.read_csv(key)
    # print(df)
    # print(value)
    # print(type(data[key]))
    for i in data[key]:
        # k,v = i
        print(i)


        # print(type(i))
        # for j in i.items():
        #     print(j)
        # if(type(i)==str):
        #     # func_call = eval(i)
        #     # print(func_call(df))
        #     print(i)
        
        
