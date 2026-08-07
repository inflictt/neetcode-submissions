class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numSet = set(nums)   # <-- THIS LINE FIXES TLE
        
        a = 0
        n = len(nums)
        max_count = 0
        
        while True:
            count = 1
            start = nums[a]
            
            backNum = start - 1
            fwdnum = start + 1
            
            while fwdnum in numSet:   # uses set now -> O(1)
                fwdnum += 1
                count += 1
            
            while backNum in numSet:  # uses set now -> O(1)
                backNum -= 1
                count += 1
            
            max_count = max(max_count, count)
            
            a += 1
            if a == n:
                return max_count
