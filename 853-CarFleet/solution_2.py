class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = sorted([(position[i], ((target - position[i]) / speed[i])) for i in range(len(position))], reverse = True)

        stack = []
        for pos, time in times:
            stack.append(time)
            if len(stack) > 1 and time <= stack[-2]:
                stack.pop()

        return len(stack)
