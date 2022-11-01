from Assignment1.ListNode import ListNode
from Assignment2.TreeNode import PrintTree, TreeNode


class Solution:
    def sortedListToBST(self, head):
        array = []
        while head:
            array.append(head.val)
            head = head.next
        res = self.traversal(array, 0, len(array) - 1)
        return res

    def traversal(self, array, left, right):
        if left > right:
            return None
        mid = left + (right - left) // 2
        midRoot = TreeNode(array[mid])
        midRoot.left = self.traversal(array, left, mid - 1)
        midRoot.right = self.traversal(array, mid + 1, right)
        return midRoot


head = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
solution = Solution()
printer = PrintTree()
printer.printTree(solution.sortedListToBST(head))
