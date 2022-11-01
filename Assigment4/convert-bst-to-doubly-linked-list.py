from Assignment2.TreeNode import TreeNode


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    head = None
    prev = None

    def treeToDoublyList(self, root):
        if not root: return None
        self.traversal(root)
        self.prev.right = self.head
        self.head.left = self.prev
        return self.head

    def traversal(self, node):
        if not node: return
        self.traversal(node.left)
        if self.prev:
            node.left = self.prev
            self.prev.right = node
        else:
            self.head = node
        self.prev = node
        self.traversal(node.right)


root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
solution = Solution()
linkedlist = solution.treeToDoublyList(root)
print(linkedlist.val)
print(linkedlist.right.val)
print(linkedlist.right.right.val)
print(linkedlist.right.left.val)
