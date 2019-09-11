#-*- coding:utf-8 -*-

"""
 Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""

# 使用递归算法
# 将每个数字提取出来，并递归算出剩余的数所组成的列表的可能解。最后加上提取出来的数字。
# Runtime = 100ms
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        if not nums:    # nums为空的情况
            return(answer)
        if len(nums) == 1:    # nums只有一个元素的情况
            answer.append(nums)
            return(answer)

        temp_list = nums[:]    # 拷贝列表用于操作
        for each_index in range(len(temp_list)):
            base_num = temp_list[each_index]    # 提取用于操作的元素
            new_nums = temp_list[:]
            new_nums.pop(each_index)    # 将操作元素删去，生成新的列表，用于递归
            temp_answer = self.permute(new_nums)    # 递归
            for each in temp_answer:    # 添加到返回列表中
                each.append(base_num)
                answer.append(each)
        return(answer)



if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3]
    ans = solution.permute(nums)
    print(ans)