from data_auditing_modified import *
import pandas as pd
import json
import random
import time
import os

# df = pd.read_csv('KaggleV2-May-2016.csv')

column_names = ['PatientId','AppointmentID','Gender']
columns_to_be_dropped = ['PatientId']

def add_time(output_file_name):
    time_now = time.ctime()
    with open(output_file_name, 'a') as file:
        file.write(time_now)
        file.write("\n\n")

def add_spacing(output_file_name):
    with open(output_file_name, 'a') as file:    
        file.write("**************")
        file.write("\n**************")
        file.write("\n**************")
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


    ## final list of functions 
    add_time(output_file_name)
    
    data_types_per_col1(df, output_file_name, column_names)
    # data_types_per_col(df, output_file_name, column_names)

    count_of_data_types1(df, output_file_name, column_names)
    # count_of_data_types(df,output_file_name)

    num_col_rows(df,output_file_name)

    get_features(df,output_file_name)

    statistical_values1(df, output_file_name, column_names)
    # statistical_values(df, output_file_name)


    #USE THIS FUNCTION CAREFULLY AS IT MIGHT RESULT IN LARGE NUMBER OR OUTPUTS
    # uniqe_value_col1(df,output_file_name,column_names)
    # uniqe_value_col(df,output_file_name)

    remove_duplicate_rows(df,output_file_name)


    count_of_each_value1(df, output_file_name, column_names)
    # count_of_each_value(df,output_file_name)

    percent_notnull1(df,output_file_name, column_names)
    # percent_notnull(df,output_file_name)

    percent_missing_values1(df,output_file_name, column_names)
    # percent_missing_values(df,output_file_name)

    finding_small_dataset(df,output_file_name)

    #please add column name according your needs. 
    #also create multiple function calls for multiple columns
    replace_string_int(df,"NEW")

    #please add column name according your needs. 
    #also create multiple function calls for multiple columns
    #please enter the range according to your needs
    df = check_range_dataset(df,'col2',10,50)


    #please add column name according your needs. 
    #also create multiple function calls for multiple columns
    #please enter the range according to your needs
    number_within_range(df,output_file_name,'col2',10,50)


    add_spacing(output_file_name)

    edited_csv = i + '_copy.csv'
    df = check_range_dataset(df,"col2",10,50)
    df = drop_columns(df, columns_to_be_dropped)

    df.to_csv(edited_csv)
    



#################################################################3


# methods_list = ['data_types','num_col_rows','get_features','statistical_values', 'frequency_of_word', 'remove_duplicate_rows','count_of_each_value','percent_notnull','percent_missing_values','finding_small_dataset','replace_string_int','check_range_dataset','number_within_range']



# replace_string_int(df)
# check_range_dataset(df)
 
## to make a copy of csv after editing
# # print(csv_coppy())
# copy_csv = output_file_names[1]+"copy.csv"
# df.to_csv("fil.csv")



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







