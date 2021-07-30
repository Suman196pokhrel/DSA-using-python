# Time Complexity of O(N**2 )
def selectionSort(arr):
     for i in range(len(arr)):
          for j in range(i+1,len(arr)):
               if arr[j] < arr[i]:
                    arr[j],arr[i] = arr[i],arr[j]
     return arr




arr = [12,45,23,51,19,8]
selectionSort(arr)
print(arr)