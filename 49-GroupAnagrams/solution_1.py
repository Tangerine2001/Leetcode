class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        groups = []
        for string in strs:
            currAnagram = [0] * 26
            for char in string:
                idx = ord(char) - 97
                currAnagram[idx] += 1

            for i, anagram in enumerate(anagrams):
                if currAnagram == anagram:
                    groups[i].append(string)
                    break
            else:
                anagrams.append(currAnagram)
                groups.append([string])
        return groups
