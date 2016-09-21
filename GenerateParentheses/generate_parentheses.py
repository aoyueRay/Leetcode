#-*- coding:utf-8 -*-

"""
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

# 以'()'为整体，依次从左到右插入到现有的字符串中，遇到重复的情况跳过
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return([])
        if n == 1:
            return(['()'])

        temp_list = []
        answer = ['()']    # n >= 2时，初始化
        init_index = 1
        parentheses = '()'

        while init_index < n:
            for each_str in answer:    # 选择需要插入的字符串
                for i in range(len(each_str)):    # 将'()'依次插入到字符串中的各个位置
                    head = each_str[:i]
                    tail = each_str[i:]
                    temp_str = head + parentheses + tail    # 截取字符串，并将'()'插入到字符串中
                    if temp_str not in temp_list:
                        temp_list.append(temp_str)    # 避免重复
            answer = temp_list[:]    # 将新的字符串列表拷贝给返回列表
            temp_list = []
            init_index += 1
        return(answer)



if __name__ == '__main__':
    solution = Solution()
    n = 2
    ans = solution.generateParenthesis(n)
    print(ans)