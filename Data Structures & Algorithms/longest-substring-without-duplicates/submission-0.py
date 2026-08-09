class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        strings = list(s)
        left = 0  # left means the start of word in s arr
        seen = set()
        ans = 0
        winLen = 0
        for right in range(0, len(s)):  # rigth = 1
            newChar = s[right]
            if newChar not in seen:  # b not in seen add it
                seen.add(newChar)
                # left wahi 0 pr rahega as
            else:  # strings[right] is in seen: #abc tk aagye wapis a aaya
                while strings[left] != newChar:
                    seen.remove(strings[left])
                    left += 1

                # remove the duplicate itself
                left += 1
                seen.add(newChar)
            winLen = max(winLen, right - left + 1)
        return winLen
