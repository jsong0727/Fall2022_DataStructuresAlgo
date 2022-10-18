from Assignment2.TreeNode import TreeNode, PrintTree


class Solution:
    def maxWidthTree(self, root):
        if not root:
            return 0
        width = 0
        que = [(root, 0)]
        while que:
            width = max(width, 1 if len(que) == 1 else que[-1][1] - que[0][1] + 1)
            cur = []
            for q in que:
                if q[0].left:
                    cur.append((q[0].left, 2 * q[1]))
                if q[0].right:
                    cur.append((q[0].right, 2 * q[1] + 1))
            que = cur
        return width


root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
solution = Solution()
print(solution.maxWidthTree(root))
print("======================")
printer = PrintTree()
printer.printTree(root, 0)