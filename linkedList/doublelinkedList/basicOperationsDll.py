

class Node:
     def __init__(self,data):
          self.prev = None
          self.data = data
          self.next = None
     

class doubleLinkedList:
     def __init__(self):
          self.head = None
          self.tail = None

     def inser_at_start(self,data):
          node = Node(data)
          if self.head is None:
               self.head = node
               self.tail = node
          
          else:
               self.head.prev = node
               node.next = self.head
               self.head = node
                             
     def insert_at_end(self,data):
          node = Node(data)
          if self.head is None:
               self.head = node
               self.tail = node
          
          else:
               self.tail.next = node
               node.prev = self.tail
               self.tail = node

     def print_dllist(self):
          if self.head is None:
               print("Linked List is Empty")
          
          else:
               itr = self.head
               values = ''
               while itr:
                    values = values +'---->'+ str(itr.data)  
                    itr = itr.next 

               print(values) 

     def get_length_dll(self):
          count = 0
          itr = self.head
          while itr:
               count +=1
               itr = itr.next

          return count


if __name__ == '__main__':
     ll = doubleLinkedList()
     
     ll.inser_at_start(11)
     ll.inser_at_start(10)
     ll.inser_at_start(9)
     ll.inser_at_start(8)
     ll.inser_at_start(7)
     ll.inser_at_start(6)

     print(ll.get_length_dll())

     ll.insert_at_end(12)
     ll.insert_at_end(13)
     ll.insert_at_end(14)
     ll.insert_at_end(15)


     ll.print_dllist()
     

