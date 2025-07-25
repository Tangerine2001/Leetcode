class Solution:
    def findMin(self, nums: list[int]) -> int:
        # idx is min if nums[idx - 1] > nums[idx]
        # we need to maintain nums[l] > nums[r], otherwise we've either missed the min or the min is at index 0
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[l] <= nums[r]:
                return nums[l]

            if nums[m - 1] > nums[m]:
                return nums[m]

            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1

        return -1
