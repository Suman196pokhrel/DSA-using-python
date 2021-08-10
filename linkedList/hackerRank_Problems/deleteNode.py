def deleteNode(head,index):
     if index > length_of_linkedlist():
          print("Index Out of range")
     
     if head is None:
          print("List Empty")

     else:
          itr = head
          for i in range(index -1):
               itr = itr.next

          itr.next = itr.next.next
     
     return head
     