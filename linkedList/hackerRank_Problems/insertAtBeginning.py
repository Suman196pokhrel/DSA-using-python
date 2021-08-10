def insertAtBeginning(head,data):
     node = Node(data)
     if head is None:
          head = node
     
     else:
          node.next = head
          head = node
     
     return head
