class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # pick not pick on total sum
        def solve(index,temp ,final,target , total):
            # total = sum(temp)
            if total>target:
                return 
            if total == target:
                # add to final list
                final.append(temp[:])
                return 
            if index >= len(nums):
                return
            # pick
            temp.append(nums[index])
            solve(index ,temp ,final,target , total+nums[index])
            # try all possibilites and then come back if not that one
            temp.pop()
            # dont pcik the one
            solve(index + 1, temp, final, target, total)

        temp , final = [],[]
        solve(0,temp ,final,target , 0)
        return final