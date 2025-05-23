class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        starting = "({["
        ending = ")}]"
        for char in s:
            if char in ending:
                target = starting[ending.index(char)]
                while stack:
                    lastChar = stack.pop()
                    if lastChar == target:
                        break
                    elif lastChar in starting:
                        return False
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0