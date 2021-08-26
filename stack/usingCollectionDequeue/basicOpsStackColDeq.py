# Note : Recomended Method for Implementing Stacks Using python, mainly Because it uses Doubly linked list for its implementation so er dont 
# have to worry about the background moving and copying of elements
# For Stack Implementation of dequeue we only use one sided Function (ex: only left insertion/deletion, assuming that left side is the opening point of stack )


from collections import deque

class Stack:
     def __init__(self):
          self.container = deque()

     def push(self,data):
          return self.container.append(data)

     def pop(self):
          return self.container.pop()

     def peek(self):
          return self.container[-1]

     def isEmpty(self):
          return len(self.container) == 0
     
     def size(self):
          return len(self.container)

     def printStack(self):
          data1 = ''
          for elem in  self.container:
               data1 = data1 + '  ' + str(elem)
          
          print(data1)


if __name__ == '__main__':
     
     s = Stack()
     s.push(11)
     s.push(22)
     s.push(33)
     s.push(44)
     s.push(55)

     s.pop()

     s.printStack()


     
