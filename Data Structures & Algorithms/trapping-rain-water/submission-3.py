class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        leftMax[0] = height[0]
        rightMax[n - 1] = height[n - 1]
        # building lft array
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        # so now at each level max height we can fill water upto woudlbe min of both arr ith index
        ans = [0] * n
        for i in range(0, n):
            ans[i] = (min(rightMax[i], leftMax[i]) - height[i]) * 1
        return sum(ans)