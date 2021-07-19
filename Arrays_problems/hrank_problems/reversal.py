arr = [11,22,33,44]

# Method 1st
# arr.reverse()
print(arr)

# Method 2nd
arr2 = []
for i in range(len(arr)-1,-1,-1):
     print(i)
     arr2.append(arr[i])

# print(f"Arr :> {arr}")
print(f"Arr1 :> {arr2}")


