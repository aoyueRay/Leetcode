#-*- coding:utf-8 -*-

"""
 Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
"""

# 先从左到右遍历列表，筛选出该点左边最大的值，记录到max_height列表中
# 再从右到左遍历列表，筛选出该点右边最大的值，同时与max_height比较，选出较小的值即为短板，保存在max_height中
# 最后重新遍历列表，选出max_height比当前点大的值，即为该点所能保存的最大水量（面积）
# Runtime = 92ms
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        max_height = [0] * length

        # 从左向右遍历列表
        left_max = 0
        for each_index in range(length):
            if height[each_index] > left_max:
                left_max = height[each_index]    # 选出左边最大的值
            max_height[each_index] = left_max    # 更新max_height列表
        # 从右向左遍历列表
        right_max = 0
        for each_index in range(length - 1,-1,-1):
            if height[each_index] > right_max:
                right_max = height[each_index]    # 选出右边最大的值
            if right_max < max_height[each_index]:    # 处理短板
                max_height[each_index] = right_max    # 将短板值保存在max_height中
        # 最后遍历列表
        area = 0
        for each_index in range(length):
            if max_height[each_index] > height[each_index]:    # 选出max_height比但前值大的点
                area += (max_height[each_index] - height[each_index])    # 计算该点能保存的最大水量，并加到返回值中
        return(area)


if __name__ == '__main__':
    solution = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    ans = solution.trap(height)
    print(ans)