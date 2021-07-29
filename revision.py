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



def is_palindrome(s):
    if len(s) == 1 or len(s) == 0 :
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False

print(is_palindrome("kayak"))

