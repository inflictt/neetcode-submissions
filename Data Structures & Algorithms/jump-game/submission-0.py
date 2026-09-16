class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0 
        for i in range(0,len(nums)-1):
            # to travel next we use gas -1
            gas = max(nums[i],gas)
            gas -= 1
            if gas<0:#fuel over
                return False
        return True