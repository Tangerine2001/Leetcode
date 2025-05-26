class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Faster for smaller target
        times = [0] * (target + 1)
        for currPos, currSpeed in zip(position, speed):
            times[currPos] = (target - currPos) / currSpeed

        currMaxTime = 0
        res = 0
        for i in range(target, -1, -1):
            if times[i] > currMaxTime:
                res += 1
                currMaxTime = times[i]
        return res

