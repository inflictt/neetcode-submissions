class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # so simple equation i  + j + k == 0
        # i+ j = -k
        # so total = i+j, target = -k
        # n1+n2 = -n3
        # first pick n3

        n = len(nums)
        ans = []  # -> [-1,0,1,2,-1,-4]
        nums = sorted(nums)  #  [-4, -1 , -1, 0, 1 ,2,]
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:  # number same as prev number
                continue
            target = -nums[i]  # taarget = -1
            # now 2 vars to n1 and n2 to be picked up from here
            n1, n2 = i + 1, n - 1  #
            while n1 < n2:
                total = nums[n1] + nums[n2]
                if total == target:  # store them
                    ans.append(
                        [nums[i], nums[n1], nums[n2]]
                    )  # should njot have dupe triplets  skip after finidn a vlaid triplet
                    n1 += 1
                    n2 -= 1
                    while n1 < n2 and nums[n1] == nums[n1 - 1]:
                        n1 += 1
                    while n1 < n2 and nums[n2] == nums[n2 + 1]:
                        n2 -= 1
                elif total < target:
                    n1 += 1
                elif total > target:
                    n2 -= 1
                # and skip the triplets

        return ans
