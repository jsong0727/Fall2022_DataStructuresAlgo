from Assignment2.TreeNode import TreeNode, PrintTree

class Solution:
    def findLeaves(self, root):
        def helper(node, result):
            if not node:
                return -1
            level = 1 + max(helper(node.left, result), helper(node.right, result))
            if len(result) < level + 1:
                result.append([])
            result[level].append(node.val)
            return level

        result = []
        helper(root, result)
        return result


root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
solution = Solution()
print(solution.findLeaves(root))
print("======================")
printer = PrintTree()
printer.printTree(root, 0)
