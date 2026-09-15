class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def check(mid, piles):
            totalHrs = 0
            curr = 0
            for i in range(0, len(piles)):
                currHr = (
                    piles[i] // mid
                )  # ceil value as if one banana left he will need full hour for that leftover
                if piles[i] % mid != 0:
                    currHr += 1
                totalHrs += currHr
            return totalHrs

        lo, hi = 1, max(piles)
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2  # no of banana he can eat in 1hr
            if check(mid, piles) <= h:
                ans = mid
                hi = mid - 1
            elif check(mid, piles) > h:  # time took is more than alloted
                lo = mid + 1
            else:
                hi = mid - 1
        return ans