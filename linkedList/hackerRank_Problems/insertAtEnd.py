def insertAtEnd(head,data):
     node = Node(data)
     if head is None:
          head = node
     
     else:
          temp = head
          while temp.next != None:
               temp = temp.next
          
          temp.next = node
     
     return head