class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class PrintTree:
    def printTree(self, tree, level=0):
        if tree:
            self.printTree(tree.left, level + 1)
            print(' ' * 4 * level + '->' + str(tree.val))
            self.printTree(tree.right, level + 1)


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
