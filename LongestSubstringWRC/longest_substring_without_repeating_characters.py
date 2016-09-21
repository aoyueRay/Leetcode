#-*- coding:utf-8 -*-

"""
Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return(0)

        p = 0    # 初始化下标
        temp = s[p]    # 初始化临时字符串
        longest = ''    # 初始化最长字符串子串
        for i in range(1,len(s)):
            if s[i] not in temp:    # 若字符不在temp中，则添加进temp
                temp += s[i]
            else:    # 若字符在temp中
                if len(temp) > len(longest):    # 先判断temp子串是否比longest子串长，若temp较长则将temp放入longest中
                    longest = temp
                p = temp.index(s[i]) + 1    # 查找字符在temp中的位置，并截取出来形成新的temp子串
                temp = temp[p:] + s[i]
        if len(temp) > len(longest):    # 判断最终temp的长度和longest的长度，较长的即为最长子字符串
            print(temp)
            return(len(temp))
        else:
            print(longest)
            return(len(longest))

solution = Solution()
s = 'dvdf'
ans = solution.lengthOfLongestSubstring(s)
print(ans)
