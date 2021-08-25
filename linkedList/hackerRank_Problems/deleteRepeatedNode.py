def removeDuplicates(llist):
    temp1 = llist
    
    
    if temp1 is None:
        return
    
    while temp1.next is not None:
        if temp1.data == temp1.next.data:
                new = temp1.next.next
                temp1.next = None
                temp1.next = new
            
        else:
            temp1 = temp1.next
            
    
    return llist
    