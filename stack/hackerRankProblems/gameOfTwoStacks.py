# BruteForce Method
#

def twoStacks(maxSum, a, b):
     moves = 0
     currSum = 0
     i = 0
     j = 0
     # Adding All possible Elements From Stack A 
     while i<len(a) and currSum+a[i] <= maxSum:
          currSum += a[i]
          i += 1
          moves +=1
     
     # Taking As many elements from Stack B 
     while j<len(b) and i >=0:
          currSum+= b[j]
          j += 1

          # After the sum now removing excess elements from Stack A 
          while i > 0 and currSum > maxSum:
               i -= 1 # Because of previous loop in A , the i is pointing one step ahead in the array
               currSum -= a[i]
          
          # Update moves
          if currSum <= maxSum and moves < i+j:
               moves = i+j
                
     return moves

     
     
     

     return moves

if __name__ == '__main__':
   

     g = int(input().strip())

     for g_itr in range(g):
          first_multiple_input = input().rstrip().split()

          n = int(first_multiple_input[0])

          m = int(first_multiple_input[1])

          maxSum = int(first_multiple_input[2])

          a = list(map(int, input().rstrip().split()))

          b = list(map(int, input().rstrip().split()))

          result = twoStacks(maxSum, a, b)

          print(str(result) + '\n')


