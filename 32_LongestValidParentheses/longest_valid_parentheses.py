#-*- coding:utf-8 -*-

"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""

# 用一个栈记录左括号和右括号的索引值
# 遇到左括号时，压栈
# 遇到右括号且与栈顶元素匹配时，弹栈
# 远到右括号，但不匹配时，压栈
# 栈元素初始化为-1,用于计算长度
# (each_index - parentheses[-1])通过下标索引来计算长度。计算的长度，是s中连续且能匹配上的子串的长度。
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return(0)    # s为空时的处理
        parentheses = [-1]    # 初始化栈,-1用于计算长度
        length = 0    # 初始化最大长度
        for each_index in range(len(s)):
            if (s[each_index] == ')') and (parentheses[-1] != -1) and (s[parentheses[-1]] == '('):    #遇到右括号，且匹配上
                parentheses.pop()    # 弹栈
                length = max(length,(each_index - parentheses[-1]))    # (each_index - parentheses[-1])是连续匹配上的字符串的长度
            else:    # 其他不匹配的情况
                parentheses.append(each_index)    # 将索引压入栈中
        return(length)



if __name__ == '__main__':
    solution = Solution()
    s = ')()()))((()))))(())()()()()(('
    s = "()()(()"
    s = ")()(()()(()(())()("
    ans = solution.longestValidParentheses(s)
    print(ans)