'''
Link : https://leetcode.com/problems/median-of-two-sorted-arrays/description
Time Complexity : O((m+n)log(m+n))
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in range(len(nums2)):
            nums1.append(nums2[i])

        nums1.sort()
        n = len(nums1)

        if n % 2 != 0:
            return nums1[n // 2]
        else:
            return (nums1[n // 2] + nums1[(n // 2) - 1]) / 2