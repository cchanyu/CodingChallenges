class MinStack(object):
    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        stack = self.stack
        min_stack = self.min_stack

        stack.append(val)

        if min_stack:
            min_stack.append(min(val, min_stack[-1]))
        else:
            min_stack.append(val)

    def pop(self):
        stack = self.stack
        min_stack = self.min_stack

        if stack:
            stack.pop()
            min_stack.pop()
        else:
            pass
    
    def top(self):
        stack = self.stack
        if stack:
            return stack[-1]
        else:
            return -1
        
    def getMin(self):
        min_stack = self.min_stack
        if min_stack:
            return min_stack[-1]
        else:
            return -1

'''
minStack is basically a stack question, 
but only thing stack doesn't support is getMin()

getMin() grabs the minimum number in the stack.
So to track this in O(1), you'd need to create a minStack.
it can't be a simple int, because it forgets older min, it has to keep track of it.

append: min(inserting value, other minStack).
pop: pop both from stack, minStack.
top: top of the stack.
getMin: top of minStack.

'''