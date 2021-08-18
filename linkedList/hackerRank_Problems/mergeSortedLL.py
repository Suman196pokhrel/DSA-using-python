# We are creating a Dummy Node that has 0 value in the beginning

def mergeLists(head1, head2):
    dummyNode = SinglyLinkedListNode(0)
    
#     Using a temp Node to point the new LList that we will create  
    temp= dummyNode


    while True:
        if head1 is None:
            temp.next = head2
            break
        
        if head2 is None:
            temp.next = head1
            break
          # Comparing values of both LLists 
        if head1.data <= head2.data:
            temp.next = head1
            head1 = head1.next
        else:
            temp.next = head2
            head2 = head2.next
        
        temp = temp.next
    
    return dummyNode.next
        