#-*- coding:utf-8 -*-

"""
Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
"""

#
# Manacher算法，时间复杂度为O(n)。
# 可参考http://www.cnblogs.com/egust/p/4580299.html
#
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        SPECIAL = '#'    # 用于特殊处理字符串使用的字符
        center = 0    # 已知对称点对应的下标索引
        right = 0    # 已知对称点的最右端的下表索引
        mirror = 0    # 所求点i关于center的对称点的下表索引
        radius = []    # 记录以每个点为中心，最长的回文半径长度。回文半径是只最左或最右的点到中心点的长度。
        max_index = 0    # 记录最大回文子串的起始位置
        max_value = 1    # 记录最长回文子串的长度

        s = SPECIAL + SPECIAL.join(s) + SPECIAL  # 对原始字符串特殊处理，消除长度可能为奇数或者偶数的影响。
        radius = [0] * len(s)

        for i in range(len(s)):
            if i == 0:
                radius[i] = 0    # 第一个字符的半径参数值为0
                continue
            if i == 1:
                radius[i] = 1    # 第二个字符的半径参数值为1
                center = 1
                right = 2    # right = center + radius[1] = 1 + 1 = 2
                continue

            # 判断i>=2的情况
            mirror = 2 * center - i    # mirror = center - (i - center)

            # 第一种情况
            # 当前点小于已知对称的最右端点
            # 且以mirror为中心的最左端点大于以center为中心的最左端点，即mirror点的回文半径小于mirror点到左端的距离。
            # mirror到center左端的长度为：right - i
            # 左端___...___mirror___...___center___...___i___...___right
            if (i < right) and (radius[mirror] < right - i):
                radius[i] = radius[mirror]
                continue

            # 第二和第三种情况，需拓展判断radius[i]
            # 第二种情况，i比right小，但是以mirror为中心的左端小于center为中心的左端，从right后一个点开始拓展判断
            # 第三种情况，i比right边界值还要大，从0开始重新判断
            # begin是拓展判断的起始位置，第二种情况下是right的后一个位置开始，第三种情况下是i的后一个位置开始
            # end是拓展判断的终止位置
            if i > right:
                begin = 1    # 第三种情况，i比right边界值还要大
            else:
                begin = right + 1 - i    # 第二种情况，i比right小，且以mirror为中心的左端小于center为中心的左端

            end = min(i,len(s) - 1 - i)    # 终止位置为i，或者最后一个字符位置

            for n in range(begin,end + 1):
                if s[i + n] != s[i - n]:
                    end = n - 1
                    break    # 以i为中心向两边判断，若字符相等则继续，不等则跳出循环。

            center = i    # 更新中心位置
            right = i + end    # 更新最右端位置
            radius[i] = end    # 更新i点的回文半径
            if end > max_value:
                max_value = end
                max_index = i - end

        max_index = radius.index(max_value)    # 获取回文半径列表中的最大值的索引，即为最长回文子串中心的下标
        answer = s[max_index - max_value:max_index + max_value + 1]    # 获取最长回文子串
        answer = answer.replace(SPECIAL,'')    # 去掉特殊处理时使用的#字符。即为最长回文子串。
        return(answer)


#
# Solution_1是暴力解法，即先求出各个子串，再判断子串是否为回文串。时间复杂度为O(N^3)。
# 解法提交时显示超时，不可取。
#
class Solution_1(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0    # 初始化子串的起始位置
        end = 0    # 初始化子串的终止位置

        if not s:
            return(None)    # 字符串为空则返回None
        if len(s) == 1:
            return(s)    # 字符串长度为1，即只有一个字符，则最长回文子串为本身

        # 通过截取字符串判断子串是否为回文串
        # sublen为子串的长度，通过长度来获取子串
        # start为子串的起始位置
        # end为子串的终止位置，其中[start:end]为子串的长度
        for sublen in range(len(s),1,-1):
            start = 0
            end = start + sublen - 1
            while end <= (len(s) - 1):
                substr = s[start:end + 1]
                if self.judgePalindrome(substr):
                    return(substr)
                start += 1
                end += 1
        return(None)

    # 判断字符串是否为回文字符串。若是返回True，若不是返回False。
    # 输入：字符串
    # 输出：bool类型的True or False
    def judgePalindrome(self,substr):
        length = len(substr)
        if length == 1:
            return(True)

        tail = length - 1    # 最后一个字符的位置

        if (length % 2):    # 若字符串长度为奇数
            middle = (length - 1) / 2
        else:    # 若字符串为偶数
            middle = length / 2 - 1

        # 首位字符进行比较
        for i in range(middle + 1):
            if substr[i] == substr[tail]:
                tail -= 1
            else:
                return(False)
        return(True)

if __name__ == '__main__':
    solution = Solution()
    s = '"ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy"'
    s = 'babcbabcbaccba'
    ans = solution.longestPalindrome(s)
    print(ans)