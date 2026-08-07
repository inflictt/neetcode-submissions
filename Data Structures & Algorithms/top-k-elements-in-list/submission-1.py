from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       # make an dict usnig counter then add the value adn keys/number in it and then upon k requirement store them into an array and then return
        # sort the counter into decreasing and then pick first k numbers only

        ans = []
        cnt = Counter(nums)
        sorted_by_value = dict(
            sorted(cnt.items(), key=lambda item: item[1], reverse=True)
        )
        cnt = 0
        for num, occur in sorted_by_value.items():
            if cnt == k:
                break
            ans.append(num)
            cnt += 1
        return ans
