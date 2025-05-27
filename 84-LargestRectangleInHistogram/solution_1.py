class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, height in enumerate(heights):
            idx = i
            while stack and height < stack[-1][1]:
                newIdx, newHeight = stack.pop()
                res = max(res, (i - newIdx) * newHeight)
                idx = newIdx
            stack.append((idx, height))
        
        for i, height in stack:
            res = max(res, (len(heights) - i) * height)
        return res

