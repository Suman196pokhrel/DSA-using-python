def sumOfN(n):
     return n*(n+1)//2

def sumOfNRecursive(n):
     if n == 1:
          return 1
     
     else:
          return sumOfNRecursive(n-1)+n
