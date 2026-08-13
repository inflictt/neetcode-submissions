class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] > target:  # 7 < 11 true then move i+1
                j -= 1
            elif matrix[i][j] < target:  # 7 < 11 true then move i+1
                i += 1

            else:  # mil gya
                return True
        return False
