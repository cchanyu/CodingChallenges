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


create an empty list
set the pointer(current) to its head

while in a loop
1. new pointer = pointer.next
2. pointer.next = list
3. list = pointer
4. pointer = new pointer
'''