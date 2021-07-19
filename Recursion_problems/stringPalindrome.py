def palindrome(s):
     if len(s) == 1 or (len(s)==2 and s[0]==s[1]):
          return True
     else:
          if s[0] == s[-1]:
               return palindrome(s[1:-1])
          else:
               return False



val = input("Enter the String to Check :> ")
print(palindrome(val))