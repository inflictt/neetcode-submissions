class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def solve(index , total , target , temp , final):
           
            if target==total:#we need to store it but uniq combo 
                final.append(temp[:])
                return 

            # base case of return if target < total 
            if index >= len(nums) or total > target:#we need to return 
                return 
            # now we need to start picking also consider the rep allowed
            temp.append(nums[index])
            # update the sum and call again on same index
            solve(index , total + nums[index] , target , temp , final)
            # now suppose we return adn not need the prev value we ned to notPic
            e = temp.pop()
            #and if value was removed we need to decrease the summ too
            solve(index + 1 , total, target , temp , final)

        index , total , target , temp , final = 0,0, target , [], []
        solve(index , total , target , temp , final)
        return final