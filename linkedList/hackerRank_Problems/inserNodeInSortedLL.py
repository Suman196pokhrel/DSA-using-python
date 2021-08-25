
def sortedInsert(llist, data):
    temp = llist
    
    if temp is None:
        temp = DoublyLinkedListNode(data)
        return temp

    elif data <= temp.data:
        node = DoublyLinkedListNode(data)
        node.next = temp
        temp.prev = node
        temp = node
        return temp
    
    else:
        node = DoublyLinkedListNode(data)
        while temp.next != None:
            if temp.data <= data and temp.next.data >= data:
                
                node.next = temp.next
                temp.next.prev = node
                
                node.prev = temp
                temp.next = node
                
                return llist
            
            else:
                temp = temp.next
        
        temp.next = node
        node.prev = temp
        
        return llist
    
    