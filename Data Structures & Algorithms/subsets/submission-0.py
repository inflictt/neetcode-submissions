class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # pick not pick
        def solve(index , nums , temp,final):
            if index >=len(nums):#store answer copy not refer
                final.append(temp[:])
                return
            
            # pick
            temp.append(nums[index])
            solve(index + 1, nums, temp, final)

            # not pick
            temp.pop()
            solve(index + 1, nums, temp, final)


        final = []
        solve(0 , nums , [],final)
        return final