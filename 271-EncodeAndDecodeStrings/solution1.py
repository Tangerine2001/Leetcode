class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        res = ""
        for string in strs:
            res += f"#{len(string)}#{string}"
        return res

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        res = []
        i = 0
        while i < len(s):
            # Skip the first '#'
            i += 1

            # Find the second '#'
            j = s.find('#', i)

            # Extract and convert the length
            length = int(s[i:j])

            # Move past the second '#'
            j += 1

            # Extract the string using the length
            res.append(s[j:j + length])

            # Move to the start of the next encoded string
            i = j + length
        return res
