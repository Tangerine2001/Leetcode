class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        for num in seen:
            if num - 1 in seen:
                continue

            i = 0
            while num + i in seen:
                res = max(res, i + 1)
                i += 1

        return res
