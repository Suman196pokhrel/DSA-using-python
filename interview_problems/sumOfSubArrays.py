# Given an array a[] of size n .Output sum of Each subArray of given
# array 

def sumOfSubArrays():
     for i in range(int(input("Enter the number of Elements :> "))):
          arr.append(int(input(f"Enter the {i} element :> ")))


     sum = 0

     for i in range(len(arr)):
          for j in range(i, len(arr)):
               sum += arr[j]


arr = []



