#-*- coding:utf-8 -*-

"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""



# 对于s中的每个元素，若 *s==*p or *p == ? ，即匹配成功，往下继续判断，指针加一
# 若 p=='*'，即匹配成功，但可能存在多个匹配的情况，定义指针指向该'*'的位置，并保存s当前的位置，p指针后移
# 若匹配失败，则检查之前p中是否有'*'存在，没有则返回False
# 若之前有'*'存在，则将p指针指向'*'的下一个位置，将s指针指向下一个保存的s的位置
# e.g.
#
# s = abed
# p = ?b*d**
# a=?，继续。b=b，继续。
# e=*，保存'*'的位置，index_star=3，保存s的位置，star_s = 3，p指针后移
# e!=d，不匹配的情况，检查是否有'*'存在，有。
# 则ss后移一位，s指针指向star_ss的位置，p指针指向index_star的后一位
# d=d，继续，s匹配完成
# 检查p中的剩余元素，如果全是'*'，返回True。还有字母或'?'存在，返回False
# Runtime = 108ms
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        index_p = 0    # 指向p的指针
        index_s = 0    # 指向s的指针
        star_s = 0    # 保存匹配上'*'时，s当前的位置
        index_star = -1    # 指向'*'的指针
        while index_s < len(s):
            # s和p的对应位置能匹配上，或p的当前位置为'?'时，匹配成功，指针后移
            if index_p < len(p) and (s[index_s] == p[index_p] or p[index_p] == '?'):
                index_s += 1
                index_p += 1
                continue
            # p的当前位置为'*'时，可能存在后续能匹配上的情况，更新各个指针
            if index_p < len(p) and p[index_p] == '*':
                index_star = index_p    # 保存当前'*'的位置
                index_p += 1    # p指针后移继续判断
                star_s = index_s    # 保存当前s字符的位置
                continue
            # 检查是否有'*'的情况存在
            if index_star != -1:
                index_p = index_star + 1    # p指针指向'*'的后一个位置，重新开始判断
                star_s += 1    # 保存又'*'存在时s位置的指针后移，重新开始判断
                index_s = star_s    # 将s指针移回来，重新开始判断
                continue
            return False    # 以上条件均不满足，即匹配不成功，返回False
        # 将s判断完毕后，检查剩余的p的情况，如果全是'*'，返回True。还有字母或'?'存在，返回False
        while index_p < len(p) and p[index_p] == '*':
            index_p += 1    # 剩余为'*'是指针后移
        if index_p == len(p):
            return True    # 若最后p指针指向最后一位，即表示剩余的p中全是'*'，返回True
        return False    # 否则返回False



if __name__ == '__main__':
    solution = Solution()
    s = 'ab'
    p = '?*'
    ans = solution.isMatch(s,p)
    print(ans)