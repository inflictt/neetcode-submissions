class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dictOfNums = Counter(nums)

        for num, occur in dictOfNums.items():
            if occur > 1:
                return num