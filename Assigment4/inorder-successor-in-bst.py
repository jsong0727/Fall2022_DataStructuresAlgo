
class Solution:
    def inorderSuccessor(self, root, p):
        res = []

        def traversal(root):
            nonlocal res
            if not root:
                return []
            traversal(root.left)
            res.append(root)
            traversal(root.right)
            return res

        if not root:
            return None
        res = traversal(root)
        for i in range(len(res) - 1):
            if res[i].val == p.val:
                return res[i + 1]
        return None


