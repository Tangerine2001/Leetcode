class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0
        l, r, lMax, rMax = 0, len(height) - 1, height[0], height[-1]

        while l < r:
            lHeight, rHeight = height[l], height[r]
            if lHeight < rHeight:
                currIdx = l
                l += 1
            else:
                currIdx = r
                r -= 1

            trapped += max(0, min(lMax, rMax) - height[currIdx])

            lMax = max(lMax, height[l])
            rMax = max(rMax, height[r])

        return trapped
