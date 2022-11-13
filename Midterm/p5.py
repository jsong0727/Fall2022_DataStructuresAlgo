# Write a function where I pass an sorted integer array  and another array
# of integers and the function returns me start indexes of those values in second array

class Solution:
    def getStartOfEachValues(self, array, values):
        res = []
        if len(array) == 0 or len(values) == 0:
            return res

        for value in values:
            left = 0
            right = len(array)-1
            while left < right:
                middle = (left + right) // 2
                if array[middle] < value:
                    left = middle + 1
                else:
                    right = middle
            if array[left] != value:
                res.append(-1)
            else:
                res.append(left)
        return res


arr = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 5, 5, 5, 8, 9, 10, 11]
values = [1, 4, 5, 10]
output = [5, -1, 11, 16]
solution = Solution()
print(solution.getStartOfEachValues(arr, values))

