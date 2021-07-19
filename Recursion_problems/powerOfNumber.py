def powerOf(a,b):
     if b == 0 :
          return 1
     return a*powerOf(a,b-1)



a,b = [int(x) for x in input("Enter the base and power :> ").split()]

print(powerOf(a,b))
