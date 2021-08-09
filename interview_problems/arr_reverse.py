# arr1 = [int(x) for x in input("Enter the number elements for an array => ").split() ]


arr1 = [1,2,3,4,5,6,7,8,9]
# First Method- Using 2nd Array and appending in reverse
arr2 = []
j = 0
for i in range(len(arr1)-1, 0):
     print(arr1[i])
     # arr2.append(arr1[len(arr1)-i-1])
# print("arr2 is ", arr2)


#Second Method: Without Second array
# start = 0
# end = len(arr1)-1
# while start < end:
#      arr1[start],arr1[end] = arr1[end], arr1[start]
#      start+=1
#      end -=1
# print(arr1)


#Third Method : Direct Slicing
# print(s[::-1])


#Fourth method: Recursion
# def reverseArr(arr, start, end):
#      if start >= end:
#           return
#      arr[start],arr[end] = arr[end], arr[start]
#      reverseArr(arr, start+1, end-1)