arr1 = [11,22,33,44,55,66,77,88,99,101]


item = int(input(f"Enter the value that you want to Search For :> "))

for i in arr1:
     if i == item:
          print(f"Your value is at {i+1} Position")
          break