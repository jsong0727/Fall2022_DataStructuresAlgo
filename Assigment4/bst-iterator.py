from Assignment2.TreeNode import TreeNode


class BSTIterator:

    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        x = node.right
        while x:
            self.stack.append(x)
            x = x.left
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
bstIterator = BSTIterator(root)
print(bstIterator.next())
print(bstIterator.next())
print(bstIterator.hasNext())
print(bstIterator.next())
print(bstIterator.hasNext())
print(bstIterator.next())
print(bstIterator.hasNext())
print(bstIterator.next())
print(bstIterator.hasNext())
