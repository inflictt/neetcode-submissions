class Solution:
    def singleNumber(self, nums: List[int]) -> int:
                # using hashmap
        hs={}
        for num in nums :
            hs[num]=hs.get(num,0)+1
        for number,occurrences in hs.items():
            if occurrences==1:
                return number
        return -1