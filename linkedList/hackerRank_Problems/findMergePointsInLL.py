# Method 1:  Using 2 loops 
# Not Efficient 

def findMergeNode(head1, head2):
    temp1 = head1
    temp2 = head2
    
    while True:
        while True:
            if temp1.next == temp2.next:
                return temp1.next.data
            
        temp1 = temp1.next
        


# Method 2: Using linked List Difference Method 
def getLength(head):
    temp = head 
    count = 0
    while temp != None:
        temp = temp.next
        count +=1
    return count


def getNode(ind, temp1, temp2):
    for i in range(ind):
        temp1 = temp1.next
    
    while temp1 and temp2:
        if temp1 == temp2:
            return temp1.data
        
        temp1= temp1.next
        temp2 = temp2.next


def findMergeNode(head1, head2):
    temp1 = head1
    temp2 = head2
    l1 = getLength(temp1)
    l2 = getLength(temp2)
    
    if l1>=l2:
        return getNode(l1-l2,temp1,temp2)
    else:
        return getNode(l2-l1,temp2,temp1)
    
    
        