class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedChars = dict()
        # its like sortedChar(ch)->mapped to array of unsorted chars of the same
        for i in range(len(strs)):
            char = strs[i]  # got eat /now to sort it
            sortedCh = "".join(sorted(char))  # became aet
            if sortedCh in sortedChars:  # means ye already key and existing
                sortedChars[sortedCh].append(char)  # means aet:[eat] daalo esa
            # else ki ye sorted char keey existing nhi h toh ab ye banao
            else:
                sortedChars[sortedCh] = []
                sortedChars[sortedCh].append(char)
        ans = []
        for key, val in sortedChars.items():
            ans.append(val)
        return ans
