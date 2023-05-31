from collections import deque


def levelOrder(self, root):
    if not root:
        return []
    
    list = []
    q = deque()
    q.append(root)

    while len(q):
        temp = []
        for i in range(len(q)):
            element = q.popleft()
            temp.append(element.val)
            if element.left:
                q.append(element.left)
            if element.right:
                q.append(element.right)
        list.append(temp)

    return list

'''
input: [3,9,20,null,null,15,7]
output: [[3],[9,20],[15,7]]

algorithm to handle this:
BFS(Breadth First Search) Algorithm

'''