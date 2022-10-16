class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        res = []

        def helper(root, depth):
            if not root: return []
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            if root.left:
                helper(root.left, depth + 1)
            if root.right:
                helper(root.right, depth + 1)

        helper(root, 0)
        return res


root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
a = Solution()
print(a.levelOrder(root))

