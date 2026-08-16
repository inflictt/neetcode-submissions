class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if target == nums[i]:
        #         return i
        # return -1
        # /brute done - o(n)
        # now binaray search log n
        # but it works only on sorted arr so i have 2 sorted halvesd both increasing
        # like 4567 as one and another as 012
        # need to find that and iterate over that
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if (
                nums[lo] <= nums[mid]
            ):  # and also target also falls in here right?:# left half is sorted
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:  # target bada hai
                    lo = mid + 1
            else:  # right half is sorted
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1
                else:  # target chota hai
                    hi = mid - 1

        return -1
