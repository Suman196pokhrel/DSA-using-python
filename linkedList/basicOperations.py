class Node:
     def __init__(self,data,next):
          self.data = data
          self.next = next


class LinkedList:
     def __init__(self):
         self.head = None

     def insert_at_beginning(self, data):
          node = Node(data,self.head)
          self.head = node


     def insert_at_middle(self,data,index):
          pass

     def insert_at_end(self,data):
          if self.head == None:
               print('LinkedList is Empty')
               node = Node(data,None)
               self.head = node
          
          
          itr = self.head
          
          while itr.next != None:
               itr = itr.next

          itr.next = Node(data,None)

     def print_data(self):
          if self.head == None:
               print("LinkedList is Empty")
          
          
          llstr = ''
          itr = self.head
          while itr:
               llstr  =   llstr + str(itr.data)+' ----> '
               itr = itr.next
                
          print(llstr)


if __name__ == '__main__':
     ll = LinkedList()

     ll.insert_at_beginning(12)
     ll.insert_at_beginning(13)
     ll.insert_at_beginning(14)

     ll.insert_at_end(22)
     ll.insert_at_end(25)

     ll.print_data()