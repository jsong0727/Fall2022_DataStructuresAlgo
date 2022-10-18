class Solution:
    def numsSameConsecDiff(self, n: int, k: int):
        if n == 1:
            return [i for i in range(10)]

        res = []

        def dfs(n, num):
            if n == 0:
                return res.append(num)
            tail = num % 10
            next_digits = set([tail + k, tail - k])
            for digit in next_digits:
                if 0 <= digit < 10:
                    new_num = num * 10 + digit
                    dfs(n-1, new_num)
        for i in range(1, 10):
            dfs(n-1, i)
        return list(res)


solution = Solution()
print(solution.numsSameConsecDiff(3,7))
