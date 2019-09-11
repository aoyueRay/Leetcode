#-*- coding:utf-8 -*-

"""
Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container,
such that the container contains the most water.

Note: You may not slant the container.

"""

# 假设我们找到能取最大容积的纵线为 i , j (假定i<j)，那么得到的最大容积C=min(ai,aj)*(j-i)；
# 在j的右端没有一条线会比它高！
# 在i的左边也不会有比它高的线!
# 直观的解释是：容积即面积，它受长和高的影响，当长度减小时候，高必须增长才有可能提升面积。
# 所以我们从长度最长时开始递减，然后寻找更高的线来更新候补。
# 当新的线比原来的线更短时，可确定其面积不会更大，即可跳过不处理。
# 移动索引时先从短边开始移动。
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_index = 0    # 左边点的索引值
        right_index = len(height) - 1    # 右边点的索引值
        max_area = 0    # 初始化最大面积
        origin = 0    # 初始化，在移动边长时，保存用于比较大小的原索引值

        while left_index != right_index:
            area_height = min(height[left_index],height[right_index])    # 高是两边中较短的一条，即短板
            area_length = right_index - left_index    # 两点建的长度
            max_area = max(max_area,area_height * area_length)    # 值较大的一个为最大容积

            # 选择需要移动的边，从较短边开始移动
            if height[left_index] < height[right_index]:
                origin = left_index
                left_index += 1
                while height[left_index] < height[origin]:
                    left_index += 1    # 左边的边长较短时，移动左边的索引。加一，直到新索引的高度大于旧索引的高度
            else:
                origin = right_index
                right_index -= 1
                while height[right_index] < height[origin]:
                    right_index -= 1    # 右边的边长较短时，移动右边的索引。减一，直到新索引的高度大于旧索引的高度

        return(max_area)


if __name__ == '__main__':
    solution = Solution()
    height = [10,20,3,6,9,56,46,7,87,45,1]
    height = [1,2,4,3]
    ans = solution.maxArea(height)
    print(ans)