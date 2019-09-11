#-*- coding:utf-8 -*-

"""
 Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:

[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""


# 使用递归算法求解，与Permutations的解法类似
# 不同之处，增加used列表，保存已经处理过的数据，避免重复计算
# Runtime = 185ms
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        if not nums:  # nums为空的情况
            return (answer)
        if len(nums) == 1:  # nums只有一个元素的情况
            answer.append(nums)
            return (answer)

        used = []    # 存放已经计算过的数
        temp_list = nums[:]  # 拷贝列表用于操作
        for each_index in range(len(temp_list)):
            base_num = temp_list[each_index]  # 提取用于计算的元素
            if base_num in used:
                continue
            else:
                used.append(base_num)
                new_nums = temp_list[:]
                new_nums.pop(each_index)  # 将操作元素删去，生成新的列表，用于递归
                temp_answer = self.permuteUnique(new_nums)  # 递归
                for each in temp_answer:  # 添加到返回列表中
                    each.append(base_num)
                    if each not in answer:
                        answer.append(each)
        return (answer)



if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,3]
    nums = [3, 3, 0, 0, 2, 3, 2]
    ans = solution.permuteUnique(nums)
    print(ans)