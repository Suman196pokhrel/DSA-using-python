

class Node:
     def __init__(self,prev=None,data=None,next=None):
          self.prev = prev
          self.data = data
          self.next = next
     

class doubleLinkedList:
     def __init__(self):
          self.head = None

     def inser_at_start(self,data):
          node = Node(None,data,self.head)
          self.head = node

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
     
     ll.inser_at_start(data=11)
     ll.inser_at_start(data=10)
     ll.inser_at_start(data=9)
     ll.inser_at_start(data=8)
     ll.inser_at_start(data=7)
     ll.inser_at_start(data=6)

     print(ll.get_length_dll())
     
     ll.print_dllist()
     

