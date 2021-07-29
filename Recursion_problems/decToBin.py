def decToBin(n,result):
     if n == 0:
          return result
     else:
          result = str(n % 2) + result
          return decToBin(n//2,result) 

print(decToBin(35,""))

