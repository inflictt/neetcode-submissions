class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # using the mapping tric t of / and this % : factore adn remainedr
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1
        # so now. a 1d arr of elem start+end indexing
        while start <= end:
            mid = (start + end) // 2
            if matrix[mid // n][mid % n] > target:
                end = mid - 1
            elif matrix[mid // n][mid % n] < target:
                start = mid + 1
            else:
                return True
        return False
