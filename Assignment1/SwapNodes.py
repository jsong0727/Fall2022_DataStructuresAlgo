from Assignment1.ListNode import LinkedList, ListNode


class Solution:
    def swapNodes(self, head, k):
        slow, fast = head, head
        while k - 1 > 0:
            fast = fast.next
            k -= 1
        cur = fast
        while fast.next:
            slow, fast = slow.next, fast.next
        cur.val, slow.val = slow.val, cur.val

        return head

list1 = LinkedList()
a = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
list1.head = head
print(list1)
list1.head = a.swapNodes(head, 2)
print(list1)

