def binarSearch(arr,left,right,elem):
     if left > right:
          return -1

     mid  = (left +right)//2
     if elem == arr[mid]:
          return mid

     if elem < arr[mid]:
          return binarSearch(arr,left,mid-1,elem)
     
     return binarSearch(arr,mid+1,right,elem)

arr = [11,22,33,44,55,66,77,88,99]

print(binarSearch(arr,0,len(arr)-1,99))