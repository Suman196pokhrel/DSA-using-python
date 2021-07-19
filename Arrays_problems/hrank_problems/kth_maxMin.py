# BruteForce Method

k = int(input("Enter the value of k :> "))
arr = [int(x) for x in input("Enter the elements in the array :> ").split()]
temp =k

while k>0:
     max_elem = arr[0]
     min_elem = arr[0]
     for elem in arr:
          if max_elem < elem:
               max_elem = elem
          if min_elem > elem:
               min_elem = elem
     k-=1
     if k>0:
          arr.remove(max_elem)
          arr.remove(min_elem)
     
print(f"{temp}th max and min value in array are {max_elem} , {min_elem}")