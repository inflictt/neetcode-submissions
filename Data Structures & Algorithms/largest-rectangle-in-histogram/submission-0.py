class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # opit rectangle wuold be made in the rfornt and back until a hetiught less than the curr ht comes so that pint would e the point of us coun itng hte wiudfht and storign max of area
        # pse and nse to be mafe of each and evey one
        n = len(heights)
        pse, nse = [-1] * n, [n] * n
        # build pse- store index instead of vals
        stack = []
        for i in range(0, n):
            currHT = heights[i]  # got 2 as curr hrgihts adn stack null
            while stack and heights[stack[-1]] >= currHT:  # nothing in this skip
                # but if had val bigger thn currht we woul pop until a small val comes as we need that as pse
                stack.pop()
            if stack:  # means after poping we have an index value in stack
                pse[i] = stack[-1]
            stack.append(i)  # add current value too now
        # building nse now
        stack = []
        for i in range(n - 1, -1, -1):  # from behind now
            currHT = heights[i]  # got 2 as curr hrgihts adn stack null
            while stack and heights[stack[-1]] >= currHT:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(i)
        ans = 0
        for i in range(n):
            width = nse[i] - pse[i] - 1
            area = heights[i] * width
            ans = max(ans, area)

        return ans
