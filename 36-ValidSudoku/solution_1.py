class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = dict()
        rows, cols = len(board), len(board[0])

        for row in range(rows):
            seen[(row, -1)] = set()
            for col in range(cols):
                val = board[row][col]
                if val == ".":
                    continue
                
                if (-1, col) not in seen:
                    seen[(-1, col)] = set()
                if (row // 3, col // 3) not in seen:
                    seen[(row // 3, col // 3)] = set()
                
                if val in seen[(row, -1)]:
                    return False
                elif val in seen[(-1, col)]:
                    return False
                elif val in seen[(row // 3, col // 3)]:
                    return False
            
                seen[(row, -1)].add(val)
                seen[(-1, col)].add(val)
                seen[(row // 3, col // 3)].add(val)

        return True

