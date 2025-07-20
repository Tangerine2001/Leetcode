class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if k >= len(nums):
            return [max(nums)]

        stack = []
        res = []
        for i in range(len(nums)):
            while stack and nums[i] > stack[-1][1]:
                stack.pop(-1)
            stack.append((i, nums[i]))

            if i < k - 1:
                continue

            while stack[0][0] <= i - k:
                stack.pop(0)

            res.append(stack[0][1])

        return res