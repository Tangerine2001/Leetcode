class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            val = numbers[l] + numbers[r]
            if val < target:
                l += 1
            elif val > target:
                r -= 1
            else:
                return [l + 1, r + 1]

        return l + 1, r + 1
