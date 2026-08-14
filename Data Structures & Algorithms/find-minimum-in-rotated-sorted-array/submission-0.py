class Solution:
    def findMin(self, nums: List[int]) -> int:
        new = sorted(nums)
        return new[0]