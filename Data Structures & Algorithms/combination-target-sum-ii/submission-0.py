# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

#         def solve(index, total, temp, final):
#             if total == target:  # i need to add it
#                 if tuple(temp) not in self.seen:
#                     self.seen.add(tuple(temp))
#                     final.append(temp[:])
#                 return
#             if index >= len(candidates) or total > target:
#                 return

#             # pick first then explor further as no rep allowed in this one
#             temp.append(candidates[index])
#             # increase the sum
#             solve(index + 1, total + candidates[index], temp, final)
#             # pop the prev elem as not picking
#             temp.pop()
#             # Skip all duplicates of the current value
#             next_index = index + 1
#             while (next_index < len(candidates)and candidates[next_index] == candidates[index]):
#                 next_index += 1

#             solve(next_index, total, temp, final)

#         self.seen = set()

#         candidates = sorted(candidates)
#         index, total, temp, final = 0, 0, [], []
#         solve(index, total, temp, final)
#         return final


# trying to solve using for loop and decreasing target not


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def solve(index, target, curr, final):
            if target < 0:  # big value deducted
                return
            if target == 0:  # got the one we need to return
                final.append(curr[:])
                return

            # now we need to do - Pick , Explore , Not Pick
            for i in range(index, len(candidates)):
                # remoove the the same number if occured prev
                if (
                    i > index and candidates[i] == candidates[i - 1]
                ):  # as index shoudl also be counted
                    continue
                # do pick
                curr.append(candidates[i])
                # explore
                solve(i + 1, target - candidates[i], curr, final)
                # not pick
                curr.pop()

        candidates = sorted(candidates)
        index, target, curr, final = 0, target, [], []
        solve(index, target, curr, final)
        return final
