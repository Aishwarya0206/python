import pandas as pd
dictionary = {'a': [1,2,3,4], 'b': [5,6,7,8], 'c': [9, 10, 11, 12], 'd': [13, 14, 15, 16], 'e': [17,18,19,20], 'f': [21,22,23,24]}
df = pd.DataFrame(dictionary)
print(df.head())
for x, y in dictionary.items():
    print(x, y)
