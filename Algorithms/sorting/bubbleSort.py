
def bubbleSort(arr):
     n = len(arr)
     for i in range(0,n-1):
          for j in range(0,n-i-1) :
               if arr[j] > arr[j+1]:
                    arr[j] ,arr[j+1] = arr[j+1] ,arr[j]




arr = [21,11,4,3,55,66,34,74,68,121,342,43,2]
bubbleSort(arr)
print(arr)
