class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicty = {}

        for word in strs:
            key = "".join(sorted(word))

            if key in dicty:
                dicty[key].append(word)
            else:
                dicty[key] = [word]

        return list(dicty.values())
