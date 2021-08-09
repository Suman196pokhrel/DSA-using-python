# Problem:

# Isyana is given the number of visitors at her local theme park on N 
# consecutive days. The number of visitors on the i-th day is V. A day is 
# record breaking if it satisfies both of the following conditions:

# • The number of visitors on the day is strictly larger than the number of visitors on each of the previous days.

# • Either it is the last day, or the number of visitors on the day is strictly larger than the number of visitors on the following day.

# Note that the very first day could be a record breaking day!

# Please help Isyana find out the number of record breaking days.

arr = [3 ,1 ,4, 1, 5, 9,2 ,6,5]
max_val = arr[0]
n_rb_days = 0

for i in range(1,len(arr)-1):
     if arr[i] > max_val:
          max_val = arr[i]

          if (arr[i] > arr[i+1]) :
               n_rb_days +=1

print(n_rb_days) 

# Note : Above Solution doesnot pass all testcases 