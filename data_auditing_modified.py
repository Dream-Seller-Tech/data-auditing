import pandas as pd
import numpy as np
import random 
import json

#A function which calls all the other functions
## Function uniqe_value_col prints lots of data so it has been put as a comment 
def all(dataset):
    print(make_changes(dataset))
    print(data_types(dataset))
    print(num_col_rows(dataset))
    print(get_features(dataset))
    print(statistical_values(dataset))
    print(frequency_of_word(dataset))
    # print(uniqe_value_col(dataset))
    print(remove_duplicate_rows(dataset))
    print(count_of_each_value(dataset))
    print(percent_notnull(dataset))
    print(percent_missing_values(dataset))
    print(finding_small_dataset(dataset))
    print(replace_string_int(dataset))
    print(check_range_dataset(dataset))
    print(number_within_range(dataset))


#This function adds extra columns to check whether other functions are working or not
def make_changes(dataset):
        #create a new column for checking
    dataset['NEW'] = pd.Series(
        random.choices(["Yes", "No"], weights=[1, 1], k=len(dataset)), 
        index=dataset.index
    )
    # Add random values within a range to the column 'col2'
    min_value = 0
    max_value = 150
    dataset['col2'] = np.random.randint(min_value, max_value, size=len(dataset))



# Finding datatype of each column
def data_types(dataset,output_file_name):
    with open(output_file_name, 'a') as file:
        file.write("Data Types are:\n") 
    column_data_type = {}
    for column in dataset.columns:
        ctype = str(dataset[column].dtype)
        if ctype in column_data_type:
            column_data_type[ctype] += 1
        else:
            column_data_type[ctype] = 1
    with open(output_file_name, 'a') as convert_file:
        convert_file.write(json.dumps(column_data_type))

    # return type(column_data_type)


# Finding number of rows and Number of Colunms
def num_col_rows(dataset,output_file_name):
    with open(output_file_name, 'a') as file:
        file.write("\n\nThe Number of Rows and Columns are \n")
    rows = dataset.shape[0]
    columns = dataset.shape[1]
    result = ("Number of rows " + str(rows) + " and the number of columns are " + str(columns))
    with open(output_file_name, 'a') as file:
        file.write(result)


#Finding List of features of each Column
def get_features(dataset,output_file_name):
    with open(output_file_name, 'a') as file:
        file.write("\n\nThe list of features are\n")
    features = dataset.columns.tolist()
    with open(output_file_name, 'a') as convert_file:
        convert_file.write(json.dumps(features))




# Removing Duplicates
# def remove_duplicates(dataset):
#     dataset = dataset.drop_duplicates()
#     return dataset



# STATISTICAL VALUE
# Finding Statistical value of each Column
def statistical_values(dataset,output_file_name):
    for column in dataset.columns:   
        if(dataset[column].dtype == np.int64 or  dataset[column].dtype == np.int32):    
            #Mean
            mean = dataset[column].mean()
            #Median
            median = dataset[column].median()
            #Standard Deviation 
            std = dataset[column].std()
            #Minimum value of column
            minimum = dataset[column].min()
            #Maximum Value of Column
            maximum = dataset[column].max()
            #Quartile of column
            quartiles = dataset[column].quantile([0.25, 0.5, 0.75])

        else:
            continue        
        with open(output_file_name, 'a') as file:
            file.write("\n\nColumn name = " + column)
            file.write("\nMean = "+ str(mean))
            file.write("\nMedian = "+ str(median))
            file.write("\nStandard Deviation = "+ str(std))
            file.write("\nMinimum value is = "+ str(minimum))
            file.write("\nMaximum value is = "+ str(maximum))
            file.write("\nQuartile = "+ str(quartiles))

            

#This function is only for a particular column
def frequency_of_word(dataset,output_file_name):
    word_counts = dataset["Gender"].str.split().explode().value_counts()
    maxx = word_counts.max()
    minn = word_counts.min()
    # print("Word with Maximum occurance ="+word_counts.idxmax())
    # print("Word with Minimum occurance ="+word_counts.idxmin())
    with open(output_file_name, 'a') as file:
        file.write("\n\nMaximum Frequency of column")
        file.write("Max: "+ str(maxx)+" Min: "+str(minn))
    

#unique values in columns
#######did not append in the file
def uniqe_value_col(dataset):
    for column in dataset.columns:
        unique_values, frequencies = np.unique(dataset[column], return_counts=True)

        print(f"Column: {column}")
        for value, frequency in zip(unique_values, frequencies):
            print(f"Value: {value}, Frequency: {frequency}")
        print("\n")
# print(uniqe_value_col(df))


# Here to count the number of duplicate rows, we do not run the make_changes() Function
def remove_duplicate_rows(dataset,output_file_name):
    duplicate_rows = dataset[dataset.duplicated(keep=False)]
    dataset = dataset.drop_duplicates()
    print(dataset)
    # return len(duplicate_rows)
    with open(output_file_name, 'a') as file:
        file.write("\n\nNumber of Duplicate rows:"+ str(len(duplicate_rows))) 



####add the value which has minimum
def count_of_each_value1(dataset, coname,output_file_name):
    # for a single column
    value_counts = dataset[coname].value_counts()
    min_frequency = value_counts.min()
    max_frequency = value_counts.max()
    # print("Word with Maximum occurance ="+str(value_counts.idxmax()))
    # print("Word with Minimum occurance ="+str(word_counts.idxmin()))
    with open(output_file_name, 'a') as file:
        file.write("\n\nCount of each value")
        file.write("\nColumn Name : "+ coname) 
        file.write("\nMax count: "+ str(max_frequency)+" Min count: "+str(min_frequency))


#count of max and min value in each column
def count_of_each_value(dataset):
    ## for a single column
    # value_counts = dataset['Handcap'].value_counts()
    # min_frequency = value_counts.min()
    # max_frequency = value_counts.max()
    # print(value_counts)
    for column in dataset.columns:
        value_counts = dataset[column].value_counts()
        print("Column Name is :" + column)
        min_frequency = value_counts.min()
        max_frequency = value_counts.max()
        print(value_counts)
        print(min_frequency)
        print(max_frequency)
        print("\n\n")


def percent_notnull1(dataset, colname):
    val = dataset[colname].count()
    percent = ((val/len(dataset))*100)
    return("Notnull: " + str(percent))  
#percent of Not Null Values
def percent_notnull(dataset,output_file_name):
    for column in dataset.columns:
        val = dataset[column].count()
        with open(output_file_name, 'a') as file:
            file.write("\n\nName of column = " + column)
            file.write("\n")
            file.write(str((val/len(dataset))*100))

def percent_missing1(dataset, colname):
    val = dataset[colname].isnull().sum()
    percent = ((val/len(dataset))*100)
    return("Missing: " + str(percent))  
#Percentage of missing data
def percent_missing_values(dataset,output_file_name):
    for column in dataset.columns:
        val = dataset[column].isnull().sum()
        with open(output_file_name, 'a') as file:
            file.write("\n\nName of column = " + column)
            file.write("\n")
            file.write(str((val/len(dataset))*100))

#Finding a small dataset
def finding_small_dataset(dataset,output_file_name):
    res = dataset.head()
    with open(output_file_name, 'a') as file:
        file.write("\n\nSample Data : ")
        print(res, file=file)
        

#Cannot add to txt file because it updates csv
def replace_string_int(dataset):
    #save the dictionary with the values which are to be replaced
    str_to_int = {"No": 0, "Yes" :1 }
    #select the column to replace values
    dataset['NEW'] = dataset['NEW'].map(str_to_int)

#Cannot add to txt file because it updates csv
def check_range_dataset(dataset):
    low = 10
    upper = 110
    dataset = dataset[(dataset['col2'] >= low) & (dataset['col2'] <= upper)]
    return dataset


#to check number of columns within range and percentage
def number_within_range(dataset,output_file_name):
    low = 10
    upper = 110
    count = len(dataset[(dataset['col2'] >= low) & (dataset['col2'] <= upper)])
    with open(output_file_name, 'a') as file:
        file.write("\n\nNumber of rows within the range = " + str(count) )
        file.write("\nPercent within range = " +str((count/dataset.shape[0])*100))
 