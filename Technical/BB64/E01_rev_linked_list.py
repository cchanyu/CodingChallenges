def reverseList(self, head):
    list = None
    current = head

    while current:
        next_pointer = current.next # temp
        current.next = list # points to the list
        list = current # list points to current
        current = next_pointer
    
    return list