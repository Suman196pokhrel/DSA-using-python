# recursive Method 

def print_reverse(head):
     if head is None:
          return
     
     else:
          print_reverse(head.next)
          print(head.data)
