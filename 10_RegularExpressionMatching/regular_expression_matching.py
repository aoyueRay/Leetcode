#-*- coding:utf-8 -*-

"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""


# 递归调用判断，将结果保留在字典中，避免年重复判断
# Runtime = 140ms
class Solution(object):
    cache = {}    # 定义字典保存已经判定过的字符串
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if (s, p) in self.cache:    # 若字符串在字典中，直接返回结果
            return self.cache[(s, p)]

        if not p:    # 匹配规则为空时的情况
            return not s

        if len(p) == 1 or p[1] != '*':    # 先判断p的第一位为'.'或字符的情况
            self.cache[(s[1:], p[1:])] = self.isMatch(s[1:], p[1:])    # 递归调用，更新字典
            return len(s) > 0 and (p[0] == '.' or s[0] == p[0]) \
                   and self.cache[(s[1:], p[1:])]    # 满足条件时返回True
        while s and (p[0] == '.' or s[0] == p[0]):    # p的第一位匹配上时
            self.cache[(s, p[2:])] = self.isMatch(s, p[2:])    # 递归调用，更新字典
            if self.cache[(s, p[2:])]:
                return True
            s = s[1:]    # 截取字符串s
        self.cache[(s, p[2:])] = self.isMatch(s, p[2:])    # 更新字典
        return self.cache[(s, p[2:])]


# 使用python自带的正则表达式规则实现(regex)，偷懒。。。
# Runtime = 140ms
class Solution_1(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return re.match('^' + p + '$', s) != None



if __name__ == '__main__':
    solution = Solution()
    s = 'bbbba'
    p = '.*b'
    ans = solution.isMatch(s,p)
    print(ans)