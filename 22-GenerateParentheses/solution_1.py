class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(curr, left, right):
            if left > 0:
                dfs(curr + "(", left - 1, right)

            if right > left:
                dfs(curr + ")", left, right - 1)

            if left == right == 0:
                res.append(curr)

        dfs("", n, n)
        return res
