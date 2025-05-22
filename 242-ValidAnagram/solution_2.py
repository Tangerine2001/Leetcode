class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = [0] * 26
        for char in s:
            idx = ord(char) - 97
            s_chars[idx] += 1

        t_chars = [0] * 26
        for char in t:
            idx = ord(char) - 97
            t_chars[idx] += 1

        return s_chars == t_chars
