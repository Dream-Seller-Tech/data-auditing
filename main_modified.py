from data_auditing_modified import *
import pandas as pd
import json
import random
import time
import os

# df = pd.read_csv('KaggleV2-May-2016.csv')


def add_time(output_file_name):
    time_now = time.ctime()
    with open(output_file_name, 'a') as file:
        file.write(time_now)
        file.write("\n\n")

def add_spacing(output_file_name):
    with open(output_file_name, 'a') as file:
        file.write("\n\n")    
        file.write("**************")
        file.write("\n\n")

def compare_df(df1,df2):
    if df1.equals(df2):
        print("The files are identical.")
    else:
        print("The files are different.")



csv_output_file_names = ['KaggleV2-May-2016']

for i in csv_output_file_names:
    fname = i+'.csv'
    df = pd.read_csv(fname)
    # print(df)
    print("**************")
    output_file_name = i+'.txt'
    try:
        with open(output_file_name) as file:
            print("File exists")
    except FileNotFoundError:
        file = open(output_file_name,"x")
        print("file created")


    # to add extra columns to check Data auditing functions
    make_changes(df)

    #Auditing functions 
    add_time(output_file_name)
    data_types(df,output_file_name)
    data_types(df,output_file_name)
    num_col_rows(df,output_file_name)
    get_features(df,output_file_name)
    statistical_values(df,output_file_name)
    frequency_of_word(df,output_file_name)
    remove_duplicate_rows(df,output_file_name)
    count_of_each_value1(df,"Gender",output_file_name)
    percent_missing_values(df,output_file_name)
    finding_small_dataset(df,output_file_name)
    number_within_range(df,output_file_name)
    add_spacing(output_file_name)

    edited_csv = i + '_copy.csv'
    replace_string_int(df)
    check_range_dataset(df)
    df.to_csv(edited_csv)
    





# methods_list = ['data_types','num_col_rows','get_features','statistical_values', 'frequency_of_word', 'remove_duplicate_rows','count_of_each_value','percent_notnull','percent_missing_values','finding_small_dataset','replace_string_int','check_range_dataset','number_within_range']



# replace_string_int(df)
# check_range_dataset(df)
 
## to make a copy of csv after editing
# # print(csv_coppy())
# copy_csv = output_file_names[1]+"copy.csv"
# df.to_csv("fil.csv")



# print("**********************")
# compare_df(pd.read_csv('file.csv'),pd.read_csv('KaggleV2-May-2016.csv'))



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



