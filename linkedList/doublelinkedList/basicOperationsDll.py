

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
          
          # if self.head is None:
          #      self.head = Node(data = data)
          
          # else:
          #      temp = self.head
          #      while temp.next != None:
          #           temp = temp.next
               
          #      temp.next = Node()
          pass

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

     # print(ll.get_length_dll())

     ll.print_dllist()
     

