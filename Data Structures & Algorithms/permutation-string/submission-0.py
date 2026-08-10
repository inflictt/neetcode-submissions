class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr = list(s2)
        windowLength = len(s1)
        CounterS1 = Counter(s1)
        lenth = len(s2)
        for i in range(lenth - windowLength + 1):
            frame = arr[i : i + windowLength]
            CounterFrame = Counter(frame)
            if CounterFrame == CounterS1:
                return True
            else:
                continue
        # CounterFrame = Counter(frame)
        # if CounterFrame == CounterS1:
        #     return True
        return False
