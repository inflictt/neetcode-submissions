class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # brute sort and return 0th
        # nums = sorted(nums)
        # return nums[0]
        # so now using bin search
        # willl find the sorted part and pick the left value from there and store as an answer in it then will go to unsorted part as there could also be an possible answrr too
        n= len(nums)
        mini = float('inf')
        left , right = 0,n-1
        while left<=right:
            mid  = (left + right)//2
            if nums[mid]>=nums[left]:#store left and search in the other righter half
                mini = min(mini , nums[left],nums[mid])
                left = mid+1
            else:# nums[mid]<nums[left]:#store right and search in the other lefter half
                mini = min(mini , nums[right],nums[mid])
                right = mid-1
        return mini