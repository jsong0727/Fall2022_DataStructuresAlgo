from Assignment1.ListNode import ListNode, LinkedList


class Solution:
    def splitListToParts(self, head, k: int):
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        width = length // k
        remain_length = length % k
        res = []
        cur = head
        for i in range(k):
            pointer = cur
            if remain_length > 0:
                for j in range(width):
                    if cur: cur = cur.next
                if cur:
                    cur.next, cur = None, cur.next
                remain_length -= 1
                res.append(pointer)
            else:
                for j in range(width - 1):
                    if cur: cur = cur.next
                if cur:
                    cur.next, cur = None, cur.next
                res.append(pointer)
        return res


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))
list1 = LinkedList()
list1.head = head
print(list1)
a = Solution()
res = a.splitListToParts(head, 3)
for head in res:
    list1.head = head
    print(list1)

