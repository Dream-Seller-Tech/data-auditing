from Data_auditing import *
import random
import numpy as np

df = pd.read_csv('Fifa_world_cup_matches.csv')

print(remove_duplicate_rows(df))


# df['NEW'] = pd.Series(
#     random.choices(['yes', 'no'], weights=[1, 1], k=len(df)), 
#     index=df.index
# )

# print(replace_string_int(df))


min_value = 0
max_value = 150
df['col2'] = np.random.randint(min_value, max_value, size=len(df))


# print(replace_string_int(df))


print(check_range_dataset(df))