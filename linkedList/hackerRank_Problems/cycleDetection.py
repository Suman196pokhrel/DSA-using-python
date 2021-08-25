def has_cycle(head):
    temp1 = head
    temp2 = head
    
    while temp1 and temp2 and temp2.next:
       
        temp1 = temp1.next
        temp2 = temp2.next .next 
        
        if temp1 == temp2:
            return 1
        
            
    return 0   