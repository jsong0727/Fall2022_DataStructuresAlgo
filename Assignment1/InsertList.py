from Assignment1.ListNode import ListNode


class Solution:
    def insert(self, head, insertVal):

        if not head:
            node = ListNode(insertVal)
            node.next = node
            return node

        pre, cur = head, head.next
        while pre.next != head:
            if pre.val <= insertVal <= cur.val:
                break
            if pre.val > cur.val and (insertVal > pre.val or insertVal < cur.val):
                break
            pre, cur = pre.next, cur.next

        node = ListNode(insertVal)
        node.next = cur
        pre.next = node
        return head

head = ListNode(3)
head.next = ListNode(4)
head.next.next = ListNode(1)
head.next.next.next = head
a = Solution()
a.insert(head, 2)
print(head.val)
print(head.next.val)
print(head.next.next.val)
print(head.next.next.next.val)

