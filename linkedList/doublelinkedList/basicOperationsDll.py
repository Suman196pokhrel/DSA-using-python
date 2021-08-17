

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
     
     def insert_after(self,data,index):
          if index >= self.get_length_dll() or index < 0 :
               print('index Out of Range')
          
          
          else:
               node = Node(data)
               itr = self.head
               for i in range(index):
                    print(f"This is  {i} node with data {itr.data}")
                    itr = itr.next

               # Connection new node to next upcomming node  in the dll sequence
               node.next = itr.next
               itr.next.prev = node

               # Connecting new node to previous node in dll sequence
               itr.next = node
               node.prev = itr
              
     def insert_at_end(self,data):
          node = Node(data)
          if self.head is None:
               self.head = node
               self.tail = node
          
          else:
               self.tail.next = node
               node.prev = self.tail
               self.tail = node

     def delete_at_index(self,index):
          if self.head is None:
               return

          elif index >= self.get_length_dll() or index < 0:
               print("Index out of Range")
               return

          elif index==0:
               # Removing link from 2nd node to first 
               self.head.next.prev = None

               # Making the 2nd node the Head 
               self.head = self.head.next



          else:
               itr = self.head
               for _ in range(index-1):
                    itr = itr.next
               
               itr.next.next.prev = itr
               itr.next = itr.next.next

               # NOTE : we do not need to put none to prev and next pointers of the deleted node 
               # because, the above steps makes the refrence count to the deleted node Zero which means
               # now python will handel its memory and delete it 

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

     
     # ll.insert_after(6.5,0)
     ll.insert_after(6.5,0)
     ll.insert_after(7.5,2)
     ll.insert_after(8.5,4)


     ll.delete_at_index(5)
     ll.delete_at_index(5)
     ll.delete_at_index(5)
     ll.delete_at_index(5)


     ll.print_dllist()
     

