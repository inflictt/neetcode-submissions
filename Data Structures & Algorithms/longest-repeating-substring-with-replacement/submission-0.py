class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        l, r = 0, 0
        freq = {}
        while r < n:
            # s of r would be the index we would be checking for the things
            freq[s[r]] = (
                freq.get(s[r], 0) + 1
            )  # ki sof. r ki freq doh ni toh store as 0 kro then + 1 krdo
            #  so now the things is that i need to calc the winKLen and check fi
            winLen = r - l + 1
            maxFreq = max(freq.values())
            changeNeeded = winLen - maxFreq
            if (
                changeNeeded <= k
            ):  # allowing r to move fruther if not we will stop r to move
                ans = max(ans, winLen)
                r += 1

            else:  # changeNeeded <=k
                # bring l ahead and set r again at l
                # window is invalid
                freq[s[l]] -= 1
                l += 1
                r += 1

        return ans
