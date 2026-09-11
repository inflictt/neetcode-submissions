class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # l1 = len(s1)
        # l2 = len(s2)
        # cnt1 = Counter(s1)
        # if l1 > l2:
        #     return False
        # # ill have a fixed sliding window of each frame and have a freq count
        # for i in range(0, l2):
        #     window = s2[
        #         i : i + l1
        #     ]  # if this si the frame freq count and return True if all matched
        #     winCnt = Counter(window)
        #     if winCnt == cnt1:  # means the key mathch and val too return True
        #         return True
        # return False

        # trying with the sorting approach
        # sortS1 = sorted(s1)
        # l1, l2 = len(s1), len(s2)
        # if l1 > l2:
        #     return False
        # for i in range(0, l2):
        #     window = s2[i : i + l1]
        #     sortWin = sorted(window)
        #     if sortS1 == sortWin:
        #         return True
        # return False

        # just need to return the equal if i found any
        # using 26 len arr approach idea
        arr1 = [0] * 26
        n1 = len(s1)
        arr2 = [0] * 26
        n2 = len(s2)
        # so 1 means the one whose permuts i need to make and the 2 means the one on which i need to check 1
        # filling the arr1 based on freq of s1
        for ch in s1:
            arr1[ord(ch) - ord("a")] += 1
        # need to go over the s2 stirng and check for the same
        i = 0
        j = 0
        # j is itr over the n2 arr
        while j < n2:
            ch = s2[j]
            # first increase the current elem seen
            arr2[ord(ch) - ord("a")] += 1
            # check if the window got out of bounds
            bounds = j - i + 1
            if (
                bounds > n1
            ):  # need to get shrinked,i is on the left so that wuold be removed
                arr2[ord(s2[i]) - ord("a")] -= 1
                i += 1
            # check if equal or not
            if arr1 == arr2:
                return True
            j += 1
        return False
