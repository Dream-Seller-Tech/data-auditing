import pandas as pd
import numpy as np


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
          
# print(data_types(df))

# Finding number of rows and Number of Colunms
def num_col_rows(dataset):
    rows = dataset.shape[0]
    columns = dataset.shape[1]
    return ("Number of rows " + str(rows) + " and the number of columns are " + str(columns))
    
# print(num_col_rows(df))


#Finding List of features of each Column
def get_features(dataset):
    features = dataset.columns.tolist()
    return features

# print(get_features(df))



# Removing Duplicates
def remove_duplicates(dataset):
    dataset = dataset.drop_duplicates()
    return dataset

# print(remove_duplicates(df))


# STATISTICAL VALUE
# Finding Statistical value of each Column
def statistical_values(dataset):
    for column in dataset.columns:
        # Printing column name
        print("Column Name is = " +column)

        #Mean
        if(dataset[column].dtype == np.int64):
            mean = dataset[column].mean()
            print(f"Mean is = {mean}")
        else:
            continue

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


# mean = df.mean()
# print("Mean:")
# print(mean)

# # Calculate the median of each column
# median = df.median()
# print("\nMedian:")
# print(median)

# # Calculate the standard deviation of each column
# std = df.std()
# print("\nStandard Deviation:")
# print(std)

# # Calculate the minimum value of each column
# minimum = df.min()
# print("\nMinimum:")
# print(minimum)

# # Calculate the maximum value of each column
# maximum = df.max()
# print("\nMaximum:")
# print(maximum)

# # Calculate the quartiles of each column
# quartiles = df.quantile([0.25, 0.5, 0.75])
# print("\nQuartiles:")
# print(quartiles)


def sample_data(dataset):
    return dataset.head()

# print(sample_data(df))

#####editions to be made


def frequency_of_word(dataset):
    word_counts = dataset["team1"].str.split().explode().value_counts()
    maxx = word_counts.max()
    minn = word_counts.min()
    return (" "+ str(maxx)+" "+str(minn))
    
# print(frequency_of_word(df))
#for column in dataset.columns:


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


def count_of_each_value(dataset):
    ## for a single column
    # value_counts = dataset['possession team1'].value_counts()
    # min_frequency = value_counts.min()
    # max_frequency = value_counts.max()
    # print(value_counts)

    for column in dataset.columns:
        value_counts = dataset[column].value_counts()
        print("Column Name is :" + column)
        min_frequency = value_counts.min()
        max_frequency = value_counts.max()
        print(value_counts)



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

