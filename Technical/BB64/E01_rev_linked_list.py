def reverseList(self, head):
    list = None
    current = head

    while current:
        next_pointer = current.next # temp
        current.next = list # points to the list
        list = current # list points to current
        current = next_pointer
    
    return list

'''
head: 1->2->3->4->5
output: 5->4->3->2->1
'''