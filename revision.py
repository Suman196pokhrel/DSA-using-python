def sumOfN(n):
     if n==1:
          return 1
     else:
          return sumOfN(n-1)+n

def sumOfDigits(n):
     if n==0:
          return 0
     return (n%10 + sumOfDigits(int(n/10)))


def reverseString(st):
     if len(st) == 0:
          return ''
     else:
          return st[-1]+ reverseString(st[0:-1:1])

print(reverseString("My name is suman"))
# a = "suman"
# print(a[0:-1:1])