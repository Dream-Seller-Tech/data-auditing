from data_auditing import *
import pandas as pd
import yaml
import random

df = pd.read_csv('KaggleV2-May-2016.csv')
# print(df)

##create a new column for checking
# df['NEW'] = pd.Series(
#     random.choices(['yes', 'no'], weights=[1, 1], k=len(df)), 
#     index=df.index
# )

# Add random values within a range to the column 'col2'
# min_value = 0
# max_value = 150
# df['col2'] = np.random.randint(min_value, max_value, size=len(df))

# # print(replace_string_int(df))

# print(df)
# print(percent_missing_values(df))


# #import YAML file in Python
with open(r"new.yaml") as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    # print(data['Name_of_students'])


# func_call = eval(data[0][0])
# print(func_call(df))

# print(type(data))
# print(data[0][0])
# for key in data:
#     # print(data[key])
#     # print(value)
#     print(type(data[key]))
#     for i in data[key]:
#         print(i)


# for key, value in data.items():
#     # access the key and value of each element
#     print(f"Key: {key}")
#     print(f"Value: {value}")


# Iterate through the dictionary and access each list
# for key, value in data.items():
#     if isinstance(value, list):
#         # Do something with the list
#         for item in value:
#             print(item)

# for element in data:
#     if type(data[element]) == list:
#         print("List name: ", element)
#         print(data[element])


# import yaml

# # Load the YAML file
# with open("new.yaml", 'r') as stream:
#     data = yaml.safe_load(stream)

# # Function to print values in a YAML file
def print_yaml_values(data, indent=''):

    if isinstance(data, dict):
        #name of the CSV FILE
        for key, value in data.items():
            csv = key
            print(csv)
            #Load CSV into df
            # df = pd.read_csv(csv)
            # print(df)
            # print_yaml_values((value), indent + '  ')
            # print(type(value))
            # if isinstance(value, dict):
            #     for key, value in value.items():
            #         print(key)
            #         print("...."+value)
            if isinstance(value, list):
                for item in value:
                    # print(type(item))
                    print_yaml_values(item)
                    # if isinstance (item, dict):
                    #     for key, value in item:
                    #         print(key)

    # elif isinstance(data, list):
    #     for item in data:
    #         print_yaml_values((item) , indent + '  ')
    # else:
    #     # print(str(data))
    #     print((indent) + str(data))



def print_yaml(data, indent=''):

    if isinstance(data, dict):
        #name of the CSV FILE
        for key, value in data.items():
            csv = key
            print(csv)
            #Load CSV into df
            # df = pd.read_csv(csv)
            # print(df)
            # print_yaml((value), indent + '  ')
            print(value)
    elif isinstance(data, list):
        for item in data:
            print_yaml((item) , indent + '  ')
    else:
        # print(str(data))
        print((indent) + str(data))

# # Call the function to print values
print_yaml_values(data)




# for key, value in data.items():
#     print(f"List: {key}")
    
#     # Iterate through every element of the list and print key
#     for element in value:
#         print(f"  Key: {element.keys()}")