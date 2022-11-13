# in a binary tree populate next left of a tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def populateLeft(self, root):
        def traversal(root):
            if not root:
                return
            if root.right:
                root.right.next = root.left
            if root.left:
                if root.next:
                    root.left.next = root.next.right
            traversal(root.right)
            traversal(root.left)
        traversal(root)

solution = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
solution.populateLeft(root)
print(root.val)
print(root.left.val)
print(root.right.val)
print(root.right.next.val)
print(root.left.next)
