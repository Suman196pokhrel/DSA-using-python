
from collections import deque

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


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
          
        

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result + '\n')
