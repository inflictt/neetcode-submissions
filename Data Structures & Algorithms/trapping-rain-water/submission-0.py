class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        leftMax[0] = height[0]
        rightMax[n - 1] = height[n - 1]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        ans = 0
        for i in range(0, n - 1):
            currHt = height[i]
            ht = min(leftMax[i], rightMax[i]) - currHt
            wt = 1
            area = ht * wt
            ans += area
        return ans
