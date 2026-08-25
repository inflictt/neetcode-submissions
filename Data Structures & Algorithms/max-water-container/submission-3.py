class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        # so via 2 ptr i can solve this where that ptr would be moved whose ht is small not big as big one would stay adn small should move
        i, j = 0, n - 1
        final = 0
        while i < j:
            htOfI = height[i]
            htOfJ = height[j]
            ht = min(htOfI, htOfJ)
            wt = j - i
            area = ht * wt
            final = max(area, final)
            # now we need to move the one whose ht is small
            if htOfI < htOfJ:  # move i
                i += 1
            else:
                j -= 1
        return final
