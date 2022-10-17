class Solution:
    def subsets(self, nums):
        if not nums: return [[]]
        subset = self.subsets(nums[1:])
        return self.add_to_all(nums[0], subset) + subset

    def add_to_all(self, item, nums):
        return [[item] + l for l in nums]


solution = Solution()
nums = [1, 2, 3]
print(solution.subsets(nums))
