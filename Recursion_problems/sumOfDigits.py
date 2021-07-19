def sumOfDigits(n):
     if n==0:
          return 0
     return (n%10 + sumOfDigits(int(n/10)))


num = int(input("Enter the number :> "))

print(sumOfDigits(num))