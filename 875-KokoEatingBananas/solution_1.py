class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 0, max(piles)
        minSpeed = max(piles)

        while l <= r:
            m = (l + r) // 2

            currTotal = 0
            for pile in piles:
                q, remainder = divmod(pile, m)
                currTotal += q + int(bool(remainder > 0))

            if currTotal <= h:
                minSpeed = min(minSpeed, m)
                r = m - 1
            else:
                l = m + 1

        return minSpeed
