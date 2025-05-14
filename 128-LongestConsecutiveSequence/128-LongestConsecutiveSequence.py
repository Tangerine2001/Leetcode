# Last updated: 5/14/2025, 6:49:57 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        res = 0
        for num in num_set:
            if num - 1 in num_set:
                continue

            length = 1
            while num + length in num_set:
                length += 1
            res = max(res, length)
        return res
