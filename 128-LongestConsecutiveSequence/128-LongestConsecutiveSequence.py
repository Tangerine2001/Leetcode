# Last updated: 5/14/2025, 6:47:24 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        res = 0
        for num in unique:
            if num - 1 in unique:
                continue
            
            length = 1
            while num + 1 in unique:
                length += 1
                num += 1
            res = max(res, length)
        return res