class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # so if a list len is :
        # i-> odd = median is the middle value
        # ii-> even = median is the avg of mid and mid-1 val
        # make a new list having ll the numbers in it
        i, j = 0, 0
        l1, l2 = len(nums1), len(nums2)
        newList = []
        while i < l1 and j < l2:
            if nums1[i] <= nums2[j]:
                newList.append(nums1[i])
                i += 1
            else:
                newList.append(nums2[j])
                j += 1

        if i < l1:  # l1 left so add it full now
            while i < l1:
                newList.append(nums1[i])
                i += 1
        if j < l2:  # l2 left so add it full now
            while j < l2:
                newList.append(nums2[j])
                j += 1
        # now i have made the list now just need to have the len check and return
        newLen = len(newList)
        mid = newLen // 2
        if newLen % 2 != 0:  # odd len aagyo
            return newList[mid]
        # else return avg of mid by 2
        midMinus1 = mid - 1
        avgOfTwo = newList[mid] + newList[midMinus1]
        return avgOfTwo / 2
