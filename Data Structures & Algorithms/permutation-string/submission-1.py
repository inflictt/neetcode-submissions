class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        cnt1 = Counter(s1)
        if l1>l2:
            return False
        # ill have a fixed sliding window of each frame and have a freq count 
        for i in range(0,l2):
            window = s2[i:i+l1]#if this si the frame freq count and return True if all matched    
            winCnt = Counter(window)
            if winCnt == cnt1:#means the key mathch and val too return True
                return True
        return False