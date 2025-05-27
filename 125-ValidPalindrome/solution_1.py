class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char for char in s if self.is_alphanumeric(char)]).lower()

        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def is_alphanumeric(self, char: str) -> bool:
        val = ord(char)
        if ord('A') <= val <= ord('Z') or ord('a') <= val <= ord('z') or ord('0') <= val <= ord('9'):
            return True
        return False