import pandas as pd
import numpy as np
import random 


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
def data_types(dataset):
    column_data_type = {}
    for column in dataset.columns:
        ctype = str(dataset[column].dtype)
        if ctype in column_data_type:
            column_data_type[ctype] += 1
        else:
            column_data_type[ctype] = 1
    return column_data_type


# Finding number of rows and Number of Colunms
def num_col_rows(dataset):
    rows = dataset.shape[0]
    columns = dataset.shape[1]
    return ("Number of rows " + str(rows) + " and the number of columns are " + str(columns))
    


#Finding List of features of each Column
def get_features(dataset):
    features = dataset.columns.tolist()
    return features



# Removing Duplicates
# def remove_duplicates(dataset):
#     dataset = dataset.drop_duplicates()
#     return dataset



# STATISTICAL VALUE
# Finding Statistical value of each Column
def statistical_values(dataset):
    for column in dataset.columns:
        # Printing column name
        
        #Mean
        if(dataset[column].dtype == np.int64 or  dataset[column].dtype == np.int32):
            print("Column Name is = " +column)

            #Mean
            mean = dataset[column].mean()
            print(f"Mean is = {mean}")
       
            #Median
            median = dataset[column].median()
            print(f"Median is = {median}")

            #Standard Deviation 
            std = dataset[column].std()
            print(f"Standard Deviation is = {std}")

            #Minimum value of column
            minimum = dataset[column].min()
            print(f"Minimum is = {minimum}")

            #Maximum Value of Column
            maximum = dataset[column].max()
            print(f"Maximum is = {maximum}")

            #Quartile of column
            quartiles = dataset[column].quantile([0.25, 0.5, 0.75])
            print(f"Quartiiles is = {quartiles}")
            print("\n \n")

        else:
            continue



#####editions to be made also to print the word
def frequency_of_word(dataset):
    word_counts = dataset["Gender"].str.split().explode().value_counts()
    maxx = word_counts.max()
    minn = word_counts.min()
    return ("Max: "+ str(maxx)+"  Min: "+str(minn))
    



#unique values in columns
def uniqe_value_col(dataset):
    for column in dataset.columns:
        unique_values, frequencies = np.unique(dataset[column], return_counts=True)

        print(f"Column: {column}")
        for value, frequency in zip(unique_values, frequencies):
            print(f"Value: {value}, Frequency: {frequency}")
        print("\n")
# print(uniqe_value_col(df))


def remove_duplicate_rows(dataset):
    duplicate_rows = dataset[dataset.duplicated(keep=False)]
    print("Number of Duplicate rows:", len(duplicate_rows))
    print("Duplicate rows are :")
    print(duplicate_rows)
    dataset = dataset.drop_duplicates()
    print(dataset)


####add the value which has minimum
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


def percent_notnull(dataset):
    for column in dataset.columns:
        val = dataset[column].count()
        print("Name of column = " + column)
        print((val/len(dataset))*100)

def percent_missing_values(dataset):
    for column in dataset.columns:
        val = dataset[column].isnull().sum()
        print("Name of column = " + column)
        print((val/len(dataset))*100)


def finding_small_dataset(dataset):
    print("Sample data")
    print(dataset.head())


def replace_string_int(dataset):
    #save the dictionary with the values which are to be replaced
    str_to_int = {"No": 0, "Yes" :1 }
    #select the column to replace values
    dataset['NEW'] = dataset['NEW'].map(str_to_int)


def check_range_dataset(dataset):
    low = 10
    upper = 110
    dataset = dataset[(dataset['col2'] >= low) & (dataset['col2'] <= upper)]
    print(dataset)

#to check number of columns within range and percentage
def number_within_range(dataset):
    low = 10
    upper = 110
    count = len(dataset[(dataset['col2'] >= low) & (dataset['col2'] <= upper)])
    print("Number of rows within the range = ")
    print(count)

    print("Percent within range =  ")
    print((count/dataset.shape[0])*100)