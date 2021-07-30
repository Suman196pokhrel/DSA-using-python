# Here we have to return 
# the index of the key in the Array 

def LinearSearch(key,arr):
     for i in range(len(arr)):
          if key == arr[i]:
               return i
     return -1

key = 12
arr = [11,22,33,4411,32,11,21,12]

print(LinearSearch(key,arr))
