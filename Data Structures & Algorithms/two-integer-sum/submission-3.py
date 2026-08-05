class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffStoredInSet = {}  # stiored like this value:correspnding index
        for i in range(0, len(nums)):
            number = nums[i]
            diff = target - number
            if diff in diffStoredInSet.keys():
                return [diffStoredInSet[diff],i]  # this return the index of that
            # else store that in
            diffStoredInSet[number] = i
        return [-1, -1]
