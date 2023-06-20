def getIntersectionNode(self, headA, headB):
    one = headA
    two = headB

    while one != two:
        if one is None:
            one = headB
        else:
            one = one.next

        if two is None:
            two = headA
        else:
            two = two.next
        
    return one

'''
A: a1->a2->c1->c2->c3
B: b1->b2->b3->c1->c2->c3

skipA: 2
skipB: 3
output: intersection at c1


neetcode solution:
create a Hashset
add every A into the set
check B if any matches exist


code above's solution:
one and two has headA, headB
while they arent the same:

set one = one.next, only if one is not null, else set it to headB
set two = two.next, only if two is not null, else set it to headA

'''