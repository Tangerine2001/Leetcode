class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productLeft = [nums[0]]
        productRight = [nums[-1]]

        for i in range(1, len(nums)):
            productLeft.append(productLeft[-1] * nums[i])
            productRight.insert(0, productRight[0] * nums[len(nums) - 1 - i])

        res = []
        for i in range(len(nums)):
            left = productLeft[i - 1] if i >= 1 else 1
            right = productRight[i + 1] if i + 1 < len(nums) else 1
            res.append(left * right)

        return res
