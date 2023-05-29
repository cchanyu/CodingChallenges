def binaryTreePaths(self, root):
    list = []

    def DFS(node, s):
        if s != "":
            s += "->"
        
        s += str(node.val)

        if not node.left and not node.right:
            list.append(s)
        if node.left:
            DFS(node.left, s)
        if node.right:
            DFS(node.right, s)

    DFS(root, "")
    return list

'''
root: [1,2,3,null,5]
output: ["1->2->5","1->3"]
'''