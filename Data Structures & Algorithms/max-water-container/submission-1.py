class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        # ans = []
        # for i in range(0, n):
        #     for j in range(i + 1, n):
        #         wt = j - i
        #         ht = min(height[i], height[j])
        #         area = wt * ht
        #         ans.append(area)

        # return max(ans)
        # i at 0 and j at 8
        area = -float("inf")
        j = n - 1  # at end  having ht as 7
        i = 0
        while i < n:
            wt = j - i  # wt = 9-1 = 8
            # minht = min(height[i],height[j]) #min(1,7 ) = 7
            heightI, heightJ = height[i], height[j]
            reqHt = min(heightI, heightJ)
            area = max(area, wt * reqHt)
            # if ht of i choti move that else j move
            if heightI <= heightJ:  # i chota ya equal move i
                # move i
                i += 1
            else:  # j chota to move back j
                j -= 1

        return area
