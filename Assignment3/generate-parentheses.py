class Solution:
    def generateParenthesis(self, n):
        def backtracking(left, right, curr, result):
            if left == 0 and right == 0:
                result.append("".join(curr))
            if left > 0:
                curr.append('(')
                backtracking(left - 1, right, curr, result)
                curr.pop()
            if left < right:
                curr.append(')')
                backtracking(left, right - 1, curr, result)
                curr.pop()

        result = []
        backtracking(n, n, [], result)
        return result


solution = Solution()
n = 3
print(solution.generateParenthesis(n))