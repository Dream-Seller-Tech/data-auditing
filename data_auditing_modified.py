import pandas as pd
import numpy as np
import random 
import json




#making changes in the dataset to make sure all the functions are working
#Use this for checking. Not entirely needed
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


#Drops the columns which are not needed
#LIST OF COLUMN NAMES TO BE DROPPED
def drop_columns(dataset, column_names):
    dataset = dataset.drop(columns=column_names)
    # Print the resulting DataFrame
    # print(dataset)
    return dataset

#Finding datatype of the list of columns provided
#LIST OF COLUMNS
def data_types_per_col1(dataset,output_file_name,column_names):
    with open(output_file_name, 'a') as file:
        file.write("DATA TYPES ARE:\n") 
    for column in column_names:
        ctype = str(dataset[column].dtype)
        with open(output_file_name, 'a') as file:
            file.write("column name "+column+ " is of type : "+ctype)
            file.write("\n")
    with open(output_file_name, 'a') as file:
        file.write("\n**************\n")

#Finding Datatype for all the column in a dataset
# FOR ALL COLUMNS
def data_types_per_col(dataset,output_file_name):
    with open(output_file_name, 'a') as file:
        file.write("DATA TYPES ARE:\n") 
    for column in dataset.columns:
        ctype = str(dataset[column].dtype)
        with open(output_file_name, 'a') as file:
            file.write("column name "+column+ " is of type : "+ctype)
            file.write("\n")
    with open(output_file_name, 'a') as file:
        file.write("\n**************\n")

# Finding COUNT of each kind of datatype peresnt in the list of columns
#LIST OF COLUMNS
def count_of_data_types1(dataset,output_file_name, column_names):
    with open(output_file_name, 'a') as file:
        file.write("\n\nCOUNT OF DATA TYPES ARE: \n") 
    column_data_type = {}
    for column in column_names:
        ctype = str(dataset[column].dtype)
        if ctype in column_data_type:
            column_data_type[ctype] += 1
        else:
            column_data_type[ctype] = 1
    with open(output_file_name, 'a') as file:
        file.write(json.dumps(column_data_type))
    with open(output_file_name, 'a') as file:
        file.write("\n**************\n")


# Finding COUNT of each kind of datatype peresnt in the whole CSV file
# FOR ALL COLUMNS
def count_of_data_types(dataset,output_file_name):
    with open(output_file_name, 'a') as file:
        file.write("\n\nCOUNT OF DATA TYPES ARE: \n") 
    column_data_type = {}
    for column in dataset.columns:
        ctype = str(dataset[column].dtype)
        if ctype in column_data_type:
            column_data_type[ctype] += 1
        else:
            column_data_type[ctype] = 1
    with open(output_file_name, 'a') as file:
        file.write(json.dumps(column_data_type))
        file.write("\n**************\n")



# Finding number of rows and Number of Colunms
#This Runs ONLY for the WHOLE DATASET
def num_col_rows(dataset,output_file_name):
    with open(output_file_name, 'a') as file:
        file.write("\n\nTHE NUMBER OF ROWS AND COLUMNS ARE: \n")
    rows = dataset.shape[0]
    columns = dataset.shape[1]
    result = ("Number of rows " + str(rows) + " and the number of columns are " + str(columns))
    with open(output_file_name, 'a') as file:
        file.write(result)
    with open(output_file_name, 'a') as file:
        file.write("\n**************\n")



#Finding List of features of each Column
#Runs only for ONLY WHOLE DATASET 
def get_features(dataset,output_file_name):
    with open(output_file_name, 'a') as file:
        file.write("\n\nTHE LIST OF FEATURES ARE\n")
    features = dataset.columns.tolist()
    with open(output_file_name, 'a') as file:
        file.write(json.dumps(features))
    with open(output_file_name, 'a') as file:
        file.write("\n**************\n")


# STATISTICAL VALUE
# Finding Statistical value for list of Column
# LIST OF COLUMNS
def statistical_values1(dataset,output_file_name, column_names):
    with open(output_file_name, 'a') as file:
        file.write("\n\nSTATISTICAL VALUES ARE :")
    for column in column_names:   
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
            file.write("\nColumn name = " + column)
            file.write("\nMean = "+ str(mean))
            file.write("\nMedian = "+ str(median))
            file.write("\nStandard Deviation = "+ str(std))
            file.write("\nMinimum value is = "+ str(minimum))
            file.write("\nMaximum value is = "+ str(maximum))
            file.write("\nQuartile = "+ str(quartiles))
    with open(output_file_name, 'a') as file:
        file.write("\n**************\n")

# Finding Statistical value of each Column
# FOR ALL COLUMNS
def statistical_values(dataset,output_file_name):
    with open(output_file_name, 'a') as file:
        file.write("\n\nSTATISTICAL VALUES ARE :")
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
            file.write("\nColumn name = " + column)
            file.write("\nMean = "+ str(mean))
            file.write("\nMedian = "+ str(median))
            file.write("\nStandard Deviation = "+ str(std))
            file.write("\nMinimum value is = "+ str(minimum))
            file.write("\nMaximum value is = "+ str(maximum))
            file.write("\nQuartile = "+ str(quartiles))
    with open(output_file_name, 'a') as file:
        file.write("\n**************\n")

#USE THIS FUNCTION CAREFULLY AS IT MIGHT RESULT IN LARGE NUMBER OR OUTPUTS
#This Function counts the frequecy of every unique value
#LIST OF COLUMNS
def uniqe_value_col1(dataset,output_file_name,colummn_names):
    with open(output_file_name, 'a') as file:
        file.write("\n\nUNIQUE VALUES ARE\n")
    for column in colummn_names:
        unique_values, frequencies = np.unique(dataset[column], return_counts=True)
        with open(output_file_name, 'a') as file:
            file.write(f"Column Name: {column}")
            file.write("\n")
            for value, frequency in zip(unique_values, frequencies):
                file.write(f"Value: {value}, Frequency: {frequency}")
                file.write("     ")
            file.write("\n")
    with open(output_file_name, 'a') as file:
        file.write("\n**************\n")

#USE THIS FUNCTION CAREFULLY AS IT MIGHT RESULT IN LARGE NUMBER OR OUTPUTS
#This Function counts the frequecy of every unique value
#FOR ALL COLUMNS
def uniqe_value_col(dataset,output_file_name):
    with open(output_file_name, 'a') as file:
        file.write("\n\nUNIQUE VALUES ARE\n")
    for column in dataset.columns:
        unique_values, frequencies = np.unique(dataset[column], return_counts=True)
        with open(output_file_name, 'a') as file:
            file.write(f"Column Name: {column}")
            file.write("\n")
            for value, frequency in zip(unique_values, frequencies):
                file.write(f"Value: {value}, Frequency: {frequency}")
                file.write("     ")
            file.write("\n")
    with open(output_file_name, 'a') as file:
        file.write("\n**************\n")


# Here to count the number of duplicate rows and drop them, we do not run the make_changes() Function
#Runs for WHOLE DATASET
def remove_duplicate_rows(dataset,output_file_name):
    duplicate_rows = dataset[dataset.duplicated(keep=False)]
    dataset = dataset.drop_duplicates()
    # print(dataset)
    with open(output_file_name, 'a') as file:
        file.write("\n\nNumber of Duplicate rows:"+ str(len(duplicate_rows))) 
    with open(output_file_name, 'a') as file:
        file.write("\n**************\n")
    



#Display the word with the count which occurs maximum and minimum times
#LIST OF COLUMNS 
def count_of_each_value1(dataset,output_file_name,column_names):
    with open(output_file_name, 'a') as file:
        file.write("\n\nCOUNT OF EACH VALLUE IS: ")
    for column in column_names:
        value_counts = dataset[column].value_counts()
        min_frequency = value_counts.min()
        max_frequency = value_counts.max()
        # print("Word with Maximum occurance ="+str(value_counts.idxmax()))
        # print("Word with Minimum occurance ="+str(value_counts.idxmin()))
        with open(output_file_name, 'a') as file:
            file.write("\n\nColumn Name : "+ column) 
            file.write("\nWord with Maximum occurance = "+str(value_counts.idxmax()))
            file.write("\nMax count: "+ str(max_frequency))
            file.write("\nWord with Minimum occurance = "+str(value_counts.idxmin()))
            file.write("\nMin count: "+str(min_frequency))
    with open(output_file_name, 'a') as file:
        file.write("\n**************\n")

#Display the word with the count which occurs maximum and minimum times
#ALL COLUMNS
def count_of_each_value(dataset,output_file_name):
    with open(output_file_name, 'a') as file:
        file.write("\n\nCOUNT OF EACH VALLUE IS: ")
    for column in dataset.columns:
        value_counts = dataset[column].value_counts()
        min_frequency = value_counts.min()
        max_frequency = value_counts.max()
        # print("Word with Maximum occurance ="+str(value_counts.idxmax()))
        # print("Word with Minimum occurance ="+str(value_counts.idxmin()))
        with open(output_file_name, 'a') as file:
            file.write("\n\nColumn Name : "+ column) 
            file.write("\nWord with Maximum occurance = "+str(value_counts.idxmax()))
            file.write("\nMax count: "+ str(max_frequency))
            file.write("\nWord with Minimum occurance = "+str(value_counts.idxmin()))
            file.write("\nMin count: "+str(min_frequency))
    with open(output_file_name, 'a') as file:
        file.write("\n**************\n")


#Find % of not Null values
# LIST OF COLUMNS
def percent_notnull1(dataset,output_file_name,column_names):
    with open(output_file_name, 'a') as file:
        file.write("\n\nPERCENTAGE NOT NULL")
    for column in column_names:
        val = dataset[column].count()
        with open(output_file_name, 'a') as file:
            file.write("\n\nName of column = " + column)
            file.write("\n")
            file.write(str((val/len(dataset))*100))
    with open(output_file_name, 'a') as file:
        file.write("\n**************\n")

#Find % of not Null values
# ALL THE COLUMN
def percent_notnull(dataset,output_file_name):
    with open(output_file_name, 'a') as file:
        file.write("\n\nPERCENTAGE NOT NULL")
    for column in dataset.columns:
        val = dataset[column].count()
        with open(output_file_name, 'a') as file:
            file.write("\n\nName of column = " + column)
            file.write("\n")
            file.write(str((val/len(dataset))*100))
    with open(output_file_name, 'a') as file:
        file.write("\n**************\n")


#Find % of Missing Values
#LIST OF COLUMNS
def percent_missing_values1(dataset,output_file_name,column_names):
    with open(output_file_name, 'a') as file:
        file.write("\n\nPERCENTAGE MISSING VALUES : ")
    for column in column_names:
        val = dataset[column].isnull().sum()
        with open(output_file_name, 'a') as file:
            file.write("\n\nName of column = " + column)
            file.write("\n")
            file.write(str((val/len(dataset))*100))
    with open(output_file_name, 'a') as file:
        file.write("\n**************\n")

#Find % of Missing Values
#ALL COLUMNS
def percent_missing_values(dataset,output_file_name):
    with open(output_file_name, 'a') as file:
        file.write("\n\nPERCENTAGE MISSING VALUES : ")
    for column in dataset.columns:
        val = dataset[column].isnull().sum()
        with open(output_file_name, 'a') as file:
            file.write("\n\nName of column = " + column)
            file.write("\n")
            file.write(str((val/len(dataset))*100))
    with open(output_file_name, 'a') as file:
        file.write("\n**************\n")


#ONLY FOR WHOLE DATASET
def finding_small_dataset(dataset,output_file_name):
    res = dataset.head()
    with open(output_file_name, 'a') as file:
        file.write("\n\nSample Data : ")
        print(res, file=file)
    with open(output_file_name, 'a') as file:
        file.write("\n**************\n")
        



# THE BELOW FUNCTIONS ARE FOR SPECIFIC COLUMNS AND REQUIRE SPECIFIC CHANGES.
# PLEASE MAKE THE CHANGES ACCORDINGLY
# INSTRUCTIONS ARE GIVEN ACCORDINGLY ABOVE EACH FUNCTION

#Cannot add to txt file because it updates csv
#add the necessary STRING to INT values as a dictinary shown below
def replace_string_int(dataset, col_name):
    #save the dictionary with the values which are to be replaced
    str_to_int = {"No": 0, "Yes" :1 }
    #select the column to replace values
    dataset[col_name] = dataset[col_name].map(str_to_int)


#Cannot add to txt file because it updates csv
#to make changes to the dataset by filtering the given range provided
#please change the range according to your needs
def check_range_dataset(dataset,col_name,l_range,u_range):
    low = l_range
    upper = u_range
    dataset = dataset[(dataset[col_name] >= low) & (dataset[col_name] <= upper)]
    return dataset


#to check number of columns within range and percentage
def number_within_range(dataset,output_file_name, col_name,l_range,u_range):
    with open(output_file_name, 'a') as file:
        file.write("\n\nNUMBER OF VALUES WITHIN THE GIVEN RANGE ARE : ")
    low = l_range
    upper = u_range
    count = len(dataset[(dataset[col_name] >= low) & (dataset[col_name] <= upper)])
    with open(output_file_name, 'a') as file:
        file.write("\n\nColumn Name :" +col_name)
        file.write("\nNumber of rows within the range = " + str(count) )
        file.write("\nPercent within range = " +str((count/dataset.shape[0])*100))
    with open(output_file_name, 'a') as file:
        file.write("\n**************\n")