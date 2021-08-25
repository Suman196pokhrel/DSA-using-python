def reverse(llist):
    temp = llist
    
    while temp.next != None:
        temp.next , temp.prev, temp  = temp.prev, temp.next, temp.next
        
    temp.next,temp.prev = temp.prev, None
    
    
    
    return temp 