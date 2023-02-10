from Data_auditing import *

df = pd.read_csv('Fifa_world_cup_matches.csv')
# print(df)

print(remove_duplicate_rows(df))