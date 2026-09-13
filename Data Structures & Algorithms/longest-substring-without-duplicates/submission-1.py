class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #  i need to store longest substring without rep chars
        # need to maintain a map 
        hashmap = {}
        n = len(s)
        l ,r = 0, 0
        maxi = 0 
        while r <n :
            # see a value and add to hashmap with its index
            ch = s[r] #got z add it at 0
            if ch not in hashmap:
                hashmap[ch]= r
            else:#i have seen it already i need to update maxi and move left
                # now move the left value
                l = max(l , hashmap[ch] + 1)
                hashmap[ch] = r
            maxi = max(maxi , r - l +1)
            
            r+=1
        return maxi