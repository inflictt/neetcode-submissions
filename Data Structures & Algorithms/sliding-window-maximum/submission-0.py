class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        ans = []
        deq = deque()
        for i in range(len(nums)):

            # 1. Remove expired element
            if deq and deq[0] <= i - k:
                deq.popleft()

            # 2. Remove smaller elements
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()

            # 3. Add current index
            deq.append(i)

            # 4. Window is complete
            if i >= k - 1:
                ans.append(nums[deq[0]])

        return ans
