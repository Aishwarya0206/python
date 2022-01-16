import numpy as np
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
