# Time complexity is O(log2 N)

def binarySearch(key,arr):
     start= 0
     end = len(arr) -1
     while(start <= end):
          mid = (start +end)//2
          if key == arr[mid]:
               return mid
          elif arr[mid] < key:
               start = mid +1
          else:
               end = mid -1
     return -1    



key = 12
arr= [8,10,12,21,33,44,55,66,76,89,99]

print(binarySearch(key,arr))