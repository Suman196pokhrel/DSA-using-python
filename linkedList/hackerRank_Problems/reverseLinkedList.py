def reverseLinkedList(head):
     if head is None:
          print("Linked List Empty")
     
     else:
          prev = None
          curr = head
          nxt = curr.next
          
          while curr != None:
               # Moving the Nxt pointer Forward 
               nxt = curr.next

               # Changing node Direction 
               curr.next = prev

               # Shifting the Nodes 
               prev = curr
               curr = nxt
          
          # At the end of loop our Curr pointer 
          # is pointing towards None so we have to 
          # change it 

          curr = prev
               
     return curr

