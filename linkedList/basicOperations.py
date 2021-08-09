class Node:
     def __init__(self,data,next=None):
          self.data = data
          self.next = next


class LinkedList:
     def __init__(self):
         self.head = None

     def insert_at_beginning(self, data):
          node = Node(data,self.head)
          self.head = node

     def insert_after(self,data,index):
          if index > self.get_length() or index < 0:
               raise Exception("The Given index is out or RangE")
               
          if index == 0:
               node = Node(data,self.head.next)
               self.head.next = node
               return

          itr = self.head
          for i in range(index):
               itr = itr.next
          
          node = Node(data, itr.next)
          itr.next = node


     def insert_at_end(self,data):
          if self.head is None:
               print('LinkedList is Empty')
               self.head = Node(data,None)
               return
          
          
          itr = self.head
          
          while itr.next:
               itr = itr.next

          itr.next = Node(data,None)

     def remove_at(self,index):
          if index <0 or index >= self.get_length():
               raise Exception("Not a valid INdex")
          
          if index == 0:
               self.head = self.head.next
               return

          itr = self.head
          for i in range(index-1):
               itr = itr.next

          itr.next = itr.next.next

     def print_data(self):
          if self.head == None:
               print("LinkedList is Empty")
          
          
          llstr = ''
          itr = self.head
          while itr:
               llstr  =   llstr + str(itr.data)+' ----> '
               itr = itr.next
                
          print(llstr)

     def createll_using_list(self,listData):
          self.head = None
          for data in listData:
               self.insert_at_end(data)

     def get_length(self):
          itr = self.head
          count = 0
          while itr:
               count +=1
               itr = itr.next
          return count

if __name__ == '__main__':
     ll = LinkedList()

     ll.insert_at_beginning(12)
     ll.insert_at_beginning(13)
     ll.insert_at_beginning(14)
     ll.insert_at_end(22)
     ll.insert_at_end(25)
     


     # ll Using ListData 
     # list1 = [22,33,44,55,66,77]
     # ll.createll_using_list(listData=list1)
     # ll.print_data()

     # Length of LL 
     # print(ll.get_length())


     # ll.remove_at(3)
     # ll.print_data()


     ll.insert_after(133, 4)
     ll.print_data()




