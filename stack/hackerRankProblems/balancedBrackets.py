
from collections import deque


# Complete the 'isBalanced' function below.

# Not Optimized method

def isBalanced(s):
     stack = deque()
     top = None
     for item in s:
          # print(top,item,stack)
          if len(stack)==0:
               stack.append(item)
               top = stack[-1]

          else:
               top = stack[-1]
               if top=='[':
                    if item == ']':
                         stack.pop()
                    else:
                         stack.append(item)
               
               elif top=='{':
                    if item=='}':
                         stack.pop()
                    else:
                         stack.append(item)
               else:
                    if item==')':
                         stack.pop()
                    else:
                         stack.append(item)
    
     if len(stack) == 0 :
          return 'YES'
     else:
          return 'NO'      
          
def isBalanced(S):
     stack = []
     pairs = {"{": "}", "[": "]", "(" : ")"}
     for i in S:
          if not stack:
               stack.append(i)
          elif i == pairs.get(stack[-1]):
               stack.pop()
          else:
               stack.append(i)
     return "YES" if not stack else "NO"  

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result + '\n')
