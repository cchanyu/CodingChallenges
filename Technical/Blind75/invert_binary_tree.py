'''

'''

nums = [4,2,7,1,3,6,9] # output: [4,7,2,9,6,3,1]

class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.val),
        if self.right:
            self.right.PrintTree()

    def invertTree(self,root):
        if root is None:
            return None
        
        temp = self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        root.left = temp

        return root

def main():
    root = TreeNode(4)
    root.insert(2)
    root.insert(7)
    root.insert(1)
    root.insert(3)
    root.insert(6)
    root.insert(9)
    root.invertTree(root)
    root.PrintTree()

if __name__ == '__main__':
    main()