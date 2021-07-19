a = int(input("Enter the number whose Factorial has to be calculated : > "))

def fact(n):
     if n==0 or n==1:
          return 1
     return n* fact(n-1)
print(f"Factorial of {a} is {fact(a)}")

     