class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        n = len(s)
        i, j = 0, n - 1
        
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1   
            else:
                return False
        return True  
