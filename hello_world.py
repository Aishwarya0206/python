import pandas as pd
import numpy as np
dictionary = {'a': [1,2,3,4], 'b': [5,6,7,8], 'c': [9, 10, 11, 12], 'd': [13, 14, 15, 16], 'e': [17,18,19,20], 'f': [21,22,23,24]}
df = pd.DataFrame(dictionary)
print(df.head())
for x, y in dictionary.items():
    print(x, y)
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"Array is {arr}")
arr1 = np.arange(70, 900, 7)
print(f"Another Array is {arr1}")
print(f"Mean of {arr} is {arr.mean()}")
even = []
odd = []
for i in arr1:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("Even: ", even)
print("Odd: ",odd)
