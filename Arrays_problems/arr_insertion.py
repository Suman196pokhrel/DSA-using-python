arr1 = [11,22,33,44,55,66,77,88,99,101]

print(f"The Array is {arr1}")
inp = int(input(f"Enter the value from 0 to {len(arr1)-1} to insert your Value"))
val = input("Enter the value :> ")
arr1.insert(inp,val)
print(arr1)




