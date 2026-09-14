class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find the start of an sequence then check how long the sequence goes on and increment the cnt
        maxi = 0
        numsSet = set(nums)
        for i in range(0,len(nums)):
            cnt = 1 #as single number is also an seq formed
            curr = nums[i] #let say got 2 here
            # check if it is start of an sequence or not
            if curr-1 not in numsSet:#true start of an seq
                while curr+1 in numsSet:
                    curr +=1
                    cnt+=1
            else:#move ahead find a seq to start
                continue
            maxi = max(maxi,cnt)
        return maxi