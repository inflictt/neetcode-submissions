class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = rows = len(board)
        cols = len(board[0])
        seenSet = set()
        for r in range(rows):
            for c in range(cols):
                value = board[r][c]
                if value == ".":
                    continue
                # this is a value or somehting
                if value in seenSet:
                    return False

                rowText = f"elem {value} at row{r}"
                colText = f"elem {value} at col{c}"
                RowColText = f"elem {value} at row{r//3} and col {c//3}"

                if rowText in seenSet or colText in seenSet or RowColText in seenSet:
                    return False
                # else connitue storineg it and in tje end return true
                seenSet.add(rowText)
                seenSet.add(colText)
                seenSet.add(RowColText)
        return True
