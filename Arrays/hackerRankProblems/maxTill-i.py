# Given an Array a[] of size n. For Every i from
# 0 to n-1 output max[a[0],a[1],...a[i]]

arr=[]


for i in range(int(input("Enter the number of Elements :> "))):
    arr.append(int(input(f"Enter the {i} element :> ")))

max_val = arr[0]
i = int(input("Enter the ith Value :> ")) 

for j in range(i):
     if arr[j] > max_val:
          max_val = arr[j]

print(f"Max value till {i} index is {max_val}")
