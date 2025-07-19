class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        tChars = dict()
        for i in range(len(t)):
            tChars[t[i]] = tChars.get(t[i], 0) + 1

        sChars = dict()
        have, need = 0, len(tChars.keys())
        l, r = 0, 0
        minLR, minLen = [0, 0], float('inf')

        while r < len(s):
            # We can skip every right pointer that doesn't have to do with t
            if s[r] not in tChars:
                r += 1
                continue

            sChars[s[r]] = sChars.get(s[r], 0) + 1
            if sChars[s[r]] == tChars[s[r]]:
                have += 1

            while have == need:
                if s[l] not in sChars:
                    l += 1
                    continue

                if r - l + 1 < minLen:
                    minLR = [l, r]
                    minLen = r - l + 1

                sChars[s[l]] -= 1
                if sChars[s[l]] < tChars[s[l]]:
                    have -= 1
                l += 1

            r += 1

        return s[minLR[0]:minLR[1] + 1] if minLen < float('inf') else ""
