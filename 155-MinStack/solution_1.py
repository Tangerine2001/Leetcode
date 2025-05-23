class MinStack:
    def __init__(self):
        self.currMin = deque()
        self.stack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.currMin:
            self.currMin.append(min(self.currMin[-1], val))
        else:
            self.currMin.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.currMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.currMin[-1]
