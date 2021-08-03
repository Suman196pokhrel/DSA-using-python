# An arithmetic array is an array that contains at least two integers and the differences 
# between consecutive integers are equal. For example, [9, 10], [3, 3, 3], and [9, 7, 5, 3]
#  are arithmetic arrays, while [1, 3, 3, 7], [2, 1, 2], and [1, 2, 4] are not arithmetic arrays.

# Sarasvati has an array of N non-negative integers. The i-th integer of the array is A.
#  She wants to choose a contiguous arithmetic subarray from her array that has the maximum 
# length. Please help her to determine the length of the longest contiguous arithmetic subarray.

arr = [3, 4, 5]
pd = arr[1] - arr[0] 
curr_max = 2
final_max = 2

for i in range(2,len(arr)):
     if(pd == arr[i]- arr[i-1]):
          curr_max+=1
     else:
          pd = arr[i]- arr[i-1]
          curr_max = 2
     
     if curr_max > final_max:
          final_max = curr_max

print('Max length of SubArray :> ', final_max)









