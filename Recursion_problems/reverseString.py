def revStr(s):
     if len(s) == 0:
          return ''
     return (s[len(s)-1] + revStr(s[:len(s)-1]))


val = input("Enter th string you want to reverse :> ")
print(revStr(val))