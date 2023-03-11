from data_auditing_modified import *
import pandas as pd
import json
import random
import time
import os

df = pd.read_csv('KaggleV2-May-2016.csv')

file_names = ['KaggleV2-May-2016']


def add_time():
    time_now = time.ctime()
    with open('conver.txt', 'a') as file:
        file.write(time_now)
        file.write("\n\n")

def add_spacing():
    with open('conver.txt', 'a') as file:
        file.write("\n\n")    
        file.write("**************")
        file.write("\n")

def compare_df(df1,df2):
    if df1.equals(df2):
        print("The files are identical.")
    else:
        print("The files are different.")

# for i in file_names:
#     fname = i+'.csv'
#     df = pd.read_csv(fname)
#     print(df)
#     print("**************")
#     name = i+'.txt'
#     try:
#         with open(name) as f:
#             print("File exists")
#     except FileNotFoundError:
#         print("File does not exist")



##Check Remove duplicates
make_changes(df)
# methods_list = ['data_types','num_col_rows','get_features','statistical_values', 'frequency_of_word', 'remove_duplicate_rows','count_of_each_value','percent_notnull','percent_missing_values','finding_small_dataset','replace_string_int','check_range_dataset','number_within_range']

#to run number of times
for i in range(1):
    add_time()
    data_types(df)
    num_col_rows(df)
    get_features(df)
    statistical_values(df)
    frequency_of_word(df)
    remove_duplicate_rows(df)
    count_of_each_value1(df,"Gender")
    percent_missing_values(df)
    finding_small_dataset(df)
    number_within_range(df)
    add_spacing()



replace_string_int(df)
check_range_dataset(df)
 

# print(csv_coppy())
copy_csv = file_names[1]+"copy.csv"
df.to_csv("fil.csv")



print("**********************")
compare_df(pd.read_csv('file.csv'),pd.read_csv('KaggleV2-May-2016.csv'))



# To append into a text file
# for i in methods_list:
#     method= eval(i)
#     method(df)
#     with open('conver.txt', 'a') as convert_file:
#         convert_file.write(json.dumps(result))
#     # append to data.txt
#     with open('conver.txt', 'a') as file:
#         file.write("\n\n") 
#     print("\n")





# # Read the CSV files into DataFrames
# df1 = pd.read_csv("KaggleV2-May-2016.csv")
# df2 = pd.read_csv("file.csv")
# diff_df = df1.compare(df2)

# # Print the differences
# print(diff_df)



