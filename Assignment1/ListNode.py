class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        res = ""
        ptr = self.head
        while ptr:
            res += str(ptr.val) + "->"
            ptr = ptr.next
        res = res.strip("->")
        if len(res):
            return "[" + res + "]"
        else:
            return "[]"
