class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = dict()
        for char in s:
            s_chars[char] = s_chars.get(char, 0) + 1

        t_chars = dict()
        for char in t:
            t_chars[char] = t_chars.get(char, 0) + 1

        return s_chars == t_chars