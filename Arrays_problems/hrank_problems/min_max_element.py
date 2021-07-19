arr = [int(x) for x in input("Enter elements in the array:> ").split()]
max_num = arr[0]
min_num = arr[0]
for elem in arr:
     if max_num < elem:
          max_num = elem
     if min_num > elem:
          min_num = elem
     

print(arr)
print(f"Max Num : {max_num} and Min num : {min_num}")