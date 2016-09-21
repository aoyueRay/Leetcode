#-*- coding:utf-8 -*-

"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not len(strs):
            return('')    # 若列表为空，则返回空字符串
        answer = strs[0]    # 先假定最长前缀子串是第一个字符串
        for i in range(1,len(strs)):
            answer = self.compare_string(answer,strs[i])    # 将最长前缀子串依次与后一个字符串对比，获取新的最长前缀子串
        return(answer)

    # 对比两个字符串，返回最长公共前缀子串
    def compare_string(self,str_a,str_b):
        length = min(len(str_a),len(str_b))    # 判断长度是两个字符串长度中较小的那个
        output = ''    # 初始化一个返回值，即最长公共子串
        for i in range(length):
            if str_a[i] == str_b[i]:
                output = output + str_a[i]    # 若字符相等则加在输出字符串上
            else:
                break    # 若字符不相等则跳出循环
        return(output)



if __name__ == '__main__':
    solution = Solution()
    strs = ['abcdefg','abcdpoi','abcdsdbca']
    ans = solution.longestCommonPrefix(strs)
    print(ans)