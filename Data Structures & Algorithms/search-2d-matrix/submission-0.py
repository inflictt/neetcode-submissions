class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = []
        for r in matrix:
            rows.extend(r)
        lo , hi = 0 , len(rows) - 1 
        while lo<=hi:
            mid = (lo+hi)//2
            if rows[mid] == target:
                return True
            elif  rows[mid] > target:
                hi = mid -1 
            else:
                lo = mid+1
        return False