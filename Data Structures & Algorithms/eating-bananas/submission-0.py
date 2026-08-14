class Solution:
    def minEatingSpeed(self, piles: List[int], requiredH: int) -> int:
        min_k = 1
        max_k = max(piles)
        final = max_k

        def calcHours(piles, currK):
            hr = 0
            # this function will return the total hourse timee
            for i in range(len(piles)):
                val = piles[i]  # got 30
                hours = (val + currK - 1) // currK  # ceil val to be added
                # if hr%10==5:
                #     hr +=0.5
                hr += hours
            return hr

        while min_k <= max_k:
            currK = (min_k + max_k) // 2
            currHoursOfK = calcHours(piles, currK)
            if currHoursOfK <= requiredH:  # got answwer but still check
                final = currK
                max_k = currK - 1
            else:  # currHoursOfK <= requiredH  jyada time lgra hai is k ke liye
                min_k = currK + 1
        return final
