class Solution:
    def findMin(self, nums):
        start1 =start2 = nums[0] #3 
        end1 = end2 = nums[-1] # 2
        #    end1 and  start1 to be calc now 
        j = -1
        for i in range(1,len(nums)):
            # jb tk increasing hai badhaao
            if nums[i] >= nums[i-1]:#good move
                continue
            else:
                j = i
                end1 = nums[i]
                break 
        start2= nums[j] #gave 1 in j 
        # now 
        # start1 and end1 are 3 and 5
        # start2 and end2 are 1 and 2 
        if start1 < start2:
            return start1
        else:
            return start2