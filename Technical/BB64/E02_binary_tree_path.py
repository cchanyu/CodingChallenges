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


depth first search: recursive til end is reached
DFS(root, "") first

enters the DFS func:
if there is #, s will += -> arrow.
if there is no #, it'll not add anything

s += add node's value

if it's a leaf node, it'll append(s)
if there's a side, it'll be recursively it called.

'''