class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        final = []
        ans = [] #stroing answers
        lenn = 0 #curr len of ans arr
        myset = set(nums) #for O of 1 lookup
        for i in range(len(nums)):
            # only start if the numebr si the starting of a sequnce
            number = nums[i]
            if number-1 not in myset:#let say 2-1 = 1 not in set ok true
                # now run a while loop for it 
                start = number +1 
                arr =[number]
                while start in myset :
                    arr.append(start)
                    start = start +1 
                if len(arr)>lenn:
                    lenn = len(arr)
                    final = arr
        return len(final)