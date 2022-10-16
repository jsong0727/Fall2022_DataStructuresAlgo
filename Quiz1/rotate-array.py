class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


a = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
a.rotate(nums, k)
print(nums)
