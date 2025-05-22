class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [set() for _ in range(len(nums) + 1)]
        freqs[0] = set(nums)
        freqsDict = dict()

        for num in nums:
            freqIdx = freqsDict.get(num, 0)
            freqs[freqIdx].remove(num)

            newIdx = freqIdx + 1
            freqs[newIdx].add(num)
            freqsDict[num] = newIdx

        res = []
        for i in range(len(nums), -1, -1):
            currNums = list(freqs[i])
            res.extend(currNums[:min(len(currNums), k - len(res))])
        return res

