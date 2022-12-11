class Solution:
    def groupAnagrams(self, strs):
        group = {}
        for s in strs:
            sorted_string = "".join(sorted(s))
            if sorted_string in group:
                group[sorted_string].append(s)
            else:
                group[sorted_string] = []
                group[sorted_string].append(s)
        return list(group.values())

# time: O(n)
# space: O(n)
strs = ["eat","tea","tan","ate","nat","bat"]
a = Solution()
print(a.groupAnagrams(strs))
