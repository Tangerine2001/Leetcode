class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        res = []
        i = 0
        while i < n - 2:
            if nums[i] > 0:
                break

            j, k = i + 1, n - 1
            i_num = nums[i]
            while j < k:
                j_num, k_num = nums[j], nums[k]
                val = i_num + j_num + k_num
                if val > 0:
                    k -= 1
                    while k > j and nums[k] == k_num:
                        k -= 1
                elif val < 0:
                    j += 1
                    while j < k and nums[j] == j_num:
                        j += 1
                else:
                    res.append([i_num, j_num, k_num])
                    j += 1
                    while j < k and nums[j] == j_num:
                        j += 1

                    k -= 1
                    while k > j and nums[k] == k_num:
                        k -= 1
            i += 1
            while i < n - 2 and nums[i] == i_num:
                i += 1
        return res
