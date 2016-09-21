#-*- coding:utf-8 -*-

"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""

# 先将每个元素按照组成字母的升序，重新排列，形成一个基础字符串
# 定义一个字典，字典的key值为基础字符串，对应的value值为各个元素
# 将每个重排列的元素与字典key值对比，不存在则新增，存在则在value值后面添加
# 最后遍历字典，将所有的value整合为返回列表
# Runtime = 264ms
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        answer_dict = {}
        answer = []
        init_index = 0
        while init_index < len(strs):
            base_str = strs[init_index]    # 获取字符串元素
            comp_list = list(base_str)
            comp_list.sort()
            comp_str = ''.join(comp_list)    # 将该字符串元素转换为按字母排序的字符串

            if comp_str not in answer_dict:    # 若该字母序列不在字典中，则新增一个字典对应关系
                answer_dict[comp_str] = []
            answer_dict[comp_str].append(base_str)    # 将字符串元素加入字典中
            init_index += 1    # 判断下一个字符串元素
        for each in answer_dict:    # 将字典中的元素整合到返回列表中
            answer.append(answer_dict[each])
        return(answer)



if __name__ == '__main__':
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    ans = solution.groupAnagrams(strs)
    print(ans)