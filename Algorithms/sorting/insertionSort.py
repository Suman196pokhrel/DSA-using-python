def selectionSort(arr):
     for i in range(1, len(arr)):
          temp = arr[i]
          j = i-1

          while(j >= 0 and arr[j] > temp):
               arr[j+1] = arr[j]
               j = -1

          arr[j+1] = temp
     
     return arr
        


brr = [21, 12, 3, 4, 33, 65, 76, 87, 1213, 43]

print("SelectionSort", selectionSort(brr))
