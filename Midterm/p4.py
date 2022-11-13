# 4. Sorted insert in a Link list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head, value):
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.val <= value:
            cur = cur.next
        temp = cur.next
        newNode = ListNode(value)
        cur.next = newNode
        newNode.next = temp
        return dummy.next


head = ListNode(1, ListNode(2, ListNode(4, ListNode(5))))
value = 1
solution = Solution()
solution.insert(head, value)

print(head.val)
print(head.next.val)
print(head.next.next.val)
print(head.next.next.next.val)
print(head.next.next.next.next.val)





