class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # n = len(nums)
        # # seen = dict()
        # for i in range(n):
        #     first = nums[i]
        #     diff = target - first
        #     # binary search over the arr
        #     lo, hi = i + 1, n - 1
        #     while lo <= hi:
        #         mid = (lo + hi) // 2
        #         if diff == nums[mid]:
        #             return [i + 1, mid + 1]
        #         elif diff > nums[mid]:
        #             lo = mid + 1
        #         else:
        #             hi = mid - 1
        # return [-1, -1]
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            total = nums[lo] + nums[hi]

            if total == target:
                return [lo + 1, hi + 1]
            elif total < target:
                lo += 1
            else:
                hi -= 1

        return [-1, -1]
