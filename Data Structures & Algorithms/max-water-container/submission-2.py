class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        area = -float("inf")
        i = 0
        j = n - 1

        while i < j:
            wt = j - i

            heightI, heightJ = height[i], height[j]
            reqHt = min(heightI, heightJ)

            area = max(area, wt * reqHt)

            if heightI <= heightJ:
                i += 1
            else:
                j -= 1

        return area