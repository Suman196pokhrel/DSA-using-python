class Node:
     def __init__(self,data):
          self.data = data
          self.next = None

class CircularLinkedList:
     def __init__(self):
          self.head = None
     
     def insert_at_beginning(self,data):
          node = Node(data)
          temp = self.head



     def insert_at_end(self,data):
          pass

     def printLList(self):
          pass

     def getLength(self):
          pass


if __name__ == '__main__':
     cll = CircularLinkedList()

     cll.printLList()