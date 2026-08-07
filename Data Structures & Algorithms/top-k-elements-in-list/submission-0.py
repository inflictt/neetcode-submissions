from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data=Counter(nums)
        ans = dict(data.most_common(k))
        lst = []
        for num,occur in ans.items():
            lst.append(num)
        return lst