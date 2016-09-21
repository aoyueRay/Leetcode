#-*- coding:utf-8 -*-

"""
 Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:

[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""

# 利用递归进行处理
# Runtime = 733ms
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.append(target)    # 将target加入列表中，排序，并将大于target的部分删掉
        candidates.sort(reverse=True)
        index = candidates.index(target)
        temp_list = candidates[index + 1:]    # 拷贝用于操作的列表

        answer = []
        for each_index in range(len(temp_list)):
            base_num = temp_list[each_index]    # 比较数
            new_target = target - base_num    # 新的目标值
            if new_target == 0:    # 目标值与比较值相等，加入answer中
                each_answer = [base_num]
                if each_answer not in answer:
                    answer.append(each_answer)
            else:    # 目标值大于比较值，将比较数删掉，用新的目标值，递归处理
                new_candidates = temp_list[:]
                new_candidates.pop(each_index)    # 删除比较数，pop()的参数只能是索引值
                temp_answer = self.combinationSum2(new_candidates,new_target)    # 递归
                for each in temp_answer:    # 加入到answer中，避免重复
                    each.append(base_num)
                    each.sort()
                    if each not in answer:
                        answer.append(each)
        return(answer)



if __name__ == '__main__':
    solution = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    ans = solution.combinationSum2(candidates,target)
    print(ans)