class Solution:
    def validParenthesesString(self, s):
        stack = []
        list_str = list(s)
        for i in range(len(list_str)):
            if list_str[i] == "(":
                stack.append(i)
            elif list_str[i] == ")":
                if stack:
                    stack.pop()
                else:
                    list_str[i] = ""
        for i in stack:
            list_str[i] = ""
        return "".join(list_str)
# time: O(n)
# space: O(n)
s = "lee(t(c)o)de)"
s1 = "a)b(c)d"
s2 = "))(("
a = Solution()
print(a.validParenthesesString(s1))