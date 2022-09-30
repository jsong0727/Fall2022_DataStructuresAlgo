from Assignment1.ListNode import ListNode, LinkedList


class Solution:
    def rotateRight(self, head, k):
        if not head:
            return None
        cur = head
        length = 1
        while cur.next:
            length += 1
            cur = cur.next
        k = k % length

        cur.next = head
        tempNode = head
        for _ in range(length - k - 1):
            tempNode = tempNode.next

        res = tempNode.next
        tempNode.next = None
        return res

list1 = LinkedList()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
list1.head = head
print(list1)
a = Solution()
list1.head = a.rotateRight(head,2)
print(list1)
