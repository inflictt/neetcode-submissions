class Solution:
    def subsets(self, nums):
        # code here
        def solve(index, temp, curr, final):
            if len(temp) <= index:
                final.append(curr[:])
                return
            curr.append(temp[index])
            solve(index + 1, temp, curr, final)
            curr.pop()
            solve(index + 1, temp, curr, final)

        index = 0
        temp = nums
        curr = []
        final = []
        solve(index, nums, curr, final)
        return final
