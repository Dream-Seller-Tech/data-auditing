import unittest 
import Data_auditing
from Data_auditing import *
import pandas as pd

df = pd.read_csv("KaggleV2-May-2016.csv")
# # print(df)
# print(count_of_each_value1(df))
# print(num_rows1(df))

class Testcalc(unittest.TestCase):


    def test_data_types(self):
        self.assertEqual(Data_auditing.data_types1(df, 'No-show'),'object') 
        self.assertEqual(Data_auditing.data_types1(df, 'Handcap'),'int64')
        self.assertEqual(Data_auditing.data_types1(df, 'Alcoholism'),'int64')

    def test_num_col_rows1(self):
        self.assertEqual(Data_auditing.num_col_rows1(df),"110527 14")

    def test_get_fetures(self):
        ar= ['PatientId', 'AppointmentID', 'Gender', 'ScheduledDay', 'AppointmentDay', 'Age', 'Neighbourhood', 'Scholarship', 'Hipertension', 'Diabetes', 'Alcoholism', 'Handcap', 'SMS_received', 'No-show']
        self.assertEqual(Data_auditing.get_features(df), ar)
    
    def test_frequency_of_words(self):
        self.assertEqual(Data_auditing.frequency_of_word(df), "Max: 11596 Min: 1")

    def test_remove_duplicate_rows(self):
        self.assertEqual(Data_auditing.remove_duplicate_rows(df),5)
    
    def test_count_of_each_value1(self):
        self.assertEqual(Data_auditing.count_of_each_value1(df, 'Handcap'), "Max count: 108286 Min count: 3")

    def test_percent_notnull1(self):
        self.assertEqual(Data_auditing.percent_notnull1(df, 'Handcap'), "Notnull: 100.0")

    def test_percent_missing1(self):
        self.assertEqual(Data_auditing.percent_missing1(df, 'Handcap'), "Missing: 0.0")

    

    