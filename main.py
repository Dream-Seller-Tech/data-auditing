from Data_auditing import *
import pandas as pd
import yaml
import random

df = pd.read_csv('KaggleV2-May-2016.csv')

with open(r"new.yaml") as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    # print(data['Name_of_students'])
c = 0

def print_yaml_values(data, indent=''):
    global c
    if c == 0:
        c = c +1
        print(c)
        if isinstance(data, dict):
            for key, value in data.items():
                csv = key
                print(csv)
                if isinstance(value, list):
                    for item in value:
                        print_yaml_values(item)
    elif c == 1:
        print(c)
        if isinstance(data, dict):
            for key, value in data.items():
                csv = key
                print(value)
                print(csv)

print_yaml_values(data)
