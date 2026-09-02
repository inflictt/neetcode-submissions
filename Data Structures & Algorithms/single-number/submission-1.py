class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # use counter as a dict and return the one with occur ==1
        Cnt = Counter(nums)
        for num , occur in Cnt.items():
            if occur==1:
                return num
        