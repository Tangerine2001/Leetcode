class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        seen = set()
        l, r = 0, 1
        seen.add(s[l])
        res = 1
        while r < len(s):
            while s[r] in seen and l < r:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            r += 1

            res = max(res, r - l)
        return res
