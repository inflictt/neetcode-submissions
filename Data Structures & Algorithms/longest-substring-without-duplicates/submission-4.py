class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # so storing value and index pair in a map 
        # evry time i see a new value ill add it and its index in the map
        # and if i see a rep value then ill increment the left ptr to 
        # l = map[currVal]. + 1
        hashmap = {}
        ans = 0
        n = len(s)
        l,r = 0 , 0
        while r<n:
            currVal = s[r] # got z in here at index r =0
            if currVal not in hashmap:
                hashmap[currVal] = r
            else:#in map already means a rep char
                l = max(hashmap[currVal] + 1,l)
                hashmap[currVal] = r
            ans = max(ans,r-l+1)
            r+=1
        return ans