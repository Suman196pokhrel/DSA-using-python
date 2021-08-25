class Node:
   def __init__(self, my_data):
      self.data = my_data
      self.next = None

class circularLinkedList:

   def __init__(self):
      self.head = None


   def add_data(self, data):
      new_node = Node(data) 
      new_node.next = self.head

      temp = self.head   

      if self.head is not None:
         while(temp.next != self.head):
            temp = temp.next
         temp.next = new_node
      else:
         new_node.next = new_node
      self.head = new_node


   def print_it(self):
      temp = self.head
      if self.head is not None:
         while(True):
            print("%d" %(temp.data)),
            temp = temp.next
            if (temp == self.head):
               break

if __name__ == '__main__':

     my_list = circularLinkedList()
     print("Elements are added to the list ")
     my_list.add_data (56)
     my_list.add_data (78)
     my_list.add_data (12)
     print("The data is : ")
     my_list.print_it()