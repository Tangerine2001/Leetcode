class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        for string in strs:
            currAnagram = [0] * 26
            for char in string:
                idx = ord(char) - 97
                currAnagram[idx] += 1
            currAnagram = tuple(currAnagram)
            groups[currAnagram] = groups.get(currAnagram, [])
            groups[currAnagram].append(string)
        return list(groups.values())
