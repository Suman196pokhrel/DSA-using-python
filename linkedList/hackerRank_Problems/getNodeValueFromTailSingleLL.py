def getNode(llist, positionFromTail):
    
    temp1 = llist
    temp2 = llist
    
    for i in range(positionFromTail):
        temp1 = temp1.next
    
    while temp1.next != None:
        temp2 = temp2.next
        temp1 = temp1.next
        
    return temp2.data
        