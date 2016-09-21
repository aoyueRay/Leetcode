#-*- coding:utf-8 -*-

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
Example 1:
    nums1 = [1, 3]
    nums2 = [2]
    The median is 2.0
Example 2:
    nums1 = [1, 2]
    nums2 = [3, 4]
    The median is (2 + 3)/2 = 2.5
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        temp = nums1 + nums2    # 合并为一个列表
        if not temp:    # 处理两个列表都为空的情况
            return(0)
        temp.sort()    # 列表排序
        length = len(temp)
        if (length % 2):    # 奇数处理
            median = temp[length / 2]
        else:    # 偶数处理
            median = (float(temp[length / 2 - 1]) + float(temp[length / 2])) / 2
        return(median)

solution = Solution()
nums1 = [2,3]
nums2 = []
ans = solution.findMedianSortedArrays(nums1,nums2)
print ans