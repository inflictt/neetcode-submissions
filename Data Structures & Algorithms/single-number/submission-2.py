class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # use counter as a dict and return the one with occur ==1
        # Cnt = Counter(nums)
        # for num , occur in Cnt.items():
        #     if occur==1:
        #         return num
        # better is that if i †take xor of 2 same number it would result as zero and if not zero one of them would be my asnwer
        ans = 0
        for val in nums:
            ans = ans ^ val  # started with 0 as that would give me the same numebr
        return ans
