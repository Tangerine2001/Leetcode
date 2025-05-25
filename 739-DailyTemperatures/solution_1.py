class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for j, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                i, _ = stack.pop()
                res[i] = j - i
            stack.append((j, temp))

        return res
