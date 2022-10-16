class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def permute(self, nums):
        self.backtracking(nums)
        return self.result

    def backtracking(self, nums):
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
            return
        for i in range(len(nums)):
            if nums[i] in self.path:
                continue
            self.path.append(nums[i])
            self.backtracking(nums)
            self.path.pop()


a = Solution()
nums = [1, 2, 3]
print(a.permute(nums))
