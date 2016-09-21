#-*- coding:utf-8 -*-

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',

determine if the input string is valid.

The brackets must close in the correct order,

"()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

# 利用栈的特性，不匹配时入栈，匹配时出栈
# 56ms
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return(True)    # 若字符串为空，返回True

        rule = {}    # 定义一个对照规则字典，左括号对应右括号，右括号对应空
        rule['('] = ')'
        rule[')'] = ''
        rule['['] = ']'
        rule[']'] = ''
        rule['{'] = '}'
        rule['}'] = ''
        temp_stack = []    # 定义一个临时栈保存括号

        for each in s:
            if (not temp_stack) or rule[temp_stack[-1]] != each:
                temp_stack.append(each)    # 栈为空，或栈中最后一个元素的对照关系与当前字符不相等，则将当前元素压栈
            else:
                temp_stack.pop()    # 若匹配上了，则将栈中最后一个元素弹出栈
        if temp_stack:
            return(False)    # 栈中仍有元素，返回False
        else:
            return(True)    # 栈中无元素，返回True

class Solution_1(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = []    # 定义左括号列表
        right = []    # 定义右括号列表
        count_left = 0    # 计算左括号的个数
        count_right = 0    # 计算右括号的个数
        for temp in s:
            if (temp == "(") or (temp == "[") or (temp == "{"):
                left.append(temp)    # 若为左括号，则放入左括号列表中
                count_left += 1    # 左括号个数加一
                right.append(self.matching(temp))    # 对应的右括号加入右括号列表
            elif (temp == ")") or (temp == "]") or (temp == "}"):
                count_right += 1    # 右括号个数加一
                if len(right) > 0:
                    comp = right.pop()    # 若右括号列表中存在元素，则弹出并进行比对
                else:
                    return(False)    # 若右括号列表中没有元素，返回False
                if temp == comp:
                    left.pop()    # 比对相等的话，将右括号列表中的元素弹出
                else:
                    return(False)    # 比对不相等，则返回False
        if count_left == count_right:
            return(True)    # 个数相同返回True
        else:
            return(False)    #个数不同返回False

    # 定义对照关系
    def matching(self,s):
        if s == "(":
            return(")")
        elif s == "[":
            return("]")
        elif s == "{":
            return("}")
        else:
            return("")


if __name__ == '__main__':
    solution = Solution_1()
    s = '()[]{}({})'
    ans = solution.isValid(s)
    print(ans)