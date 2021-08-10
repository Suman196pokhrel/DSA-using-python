from linkedList.basicOperations import Node


def insertAtIndex(head,index,data):
     node = Node(data)
     if index > length_of_llist():
          print("Index out of Range")
          return

     elif head == None:
          head = node
     
     elif index == 0:
          node.next = head
          head = node
     
     else:
          itr = head
          for i in range(index-1):
               itr = itr.next
          
          node.next = itr.next
          itr.next = node

     return head
