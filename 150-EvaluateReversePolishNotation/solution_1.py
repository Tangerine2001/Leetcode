class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }
        for token in tokens:
            if token in operators:
                r, l = int(stack.pop()), int(stack.pop())
                stack.append(operators[token](l, r))
            else:
                stack.append(token)
        return int(stack[-1])
