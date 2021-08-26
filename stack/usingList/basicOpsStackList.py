# Implementing Stack using Lists 
# NOTE: This method is not recomended , the prefered method would be to use collections.dequeue
s = [11,22,33,44,55]

def pushData(stack,data):
     stack.append(data)
     return stack

def popData(stack):
     if len(stack) != 0:
          stack.pop()
          return stack
     else:
          return 

def peekData(stack):
     return stack[-1]

def isEmpty(stack):
     if stack:
          return 0
     else:
          return 1

def printStack(stack):
     for elem in stack:
          print(elem, end=' ')


if __name__ == '__main__':
     
     pushData(s,66)
     popData(s)
     printStack(s)
     print(isEmpty(s))