#-*- coding:utf-8 -*-

"""
 Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:

[
  [7],
  [2, 2, 3]
]

"""


# 用递归的方法。依次递减，并以递减后的值为目标值。递归调用自身，获取可能解。
# Runtime = 612ms
class Solution_1(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        answer = []    # 返回列表
        temp_list = candidates[:]
        for each_index in range(len(temp_list)):
            base_num = temp_list[each_index]    # 基础数
            target_num = target - base_num    # 新的目标值
            if target_num == 0:    # 比较值与目标值相等
                temp_answer = [target]    # 自身为解的一种
                answer.append(temp_answer)
            elif target_num < 0:    # 比较值比目标值大，跳过
                continue
            else:    # 比较值小于目标值，递归调用
                other_answer = self.combinationSum(candidates,target_num)    # 以新的目标值，递归调用
                for each in other_answer:
                    each.append(base_num)    # 将基础数加入到解中
                    each.sort()    # 排序，去重
                    if each not in answer:
                        answer.append(each)
        return(answer)



if __name__ == '__main__':
    solution = Solution()
    candidates = [11, 8, 4, 3, 12, 5]
    candidates = [8, 10, 6, 3, 4, 12, 11, 5, 9]
    target = 31
    target = 28
    ans = solution.combinationSum(candidates,target)
    print(ans)