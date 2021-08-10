def print_ll(head):
     if head == None:
          print("Linked List is Empty")

     else:
          temp = head
          chars = ''
          while temp:
               chars = chars + str(temp.data) + '---->>'
               temp = temp.next
          
          print(chars)
