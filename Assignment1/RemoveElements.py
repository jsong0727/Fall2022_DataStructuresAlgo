from Assignment1.ListNode import ListNode, LinkedList


class Solution:
    def removeElements(self, head, val: int):
        dummy = cur = ListNode()
        dummy.next = head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next


list1 = LinkedList()
head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
list1.head = head
print(list1)
a = Solution()
list1.head = a.removeElements(head, 6)
print(list1)
