#-*- coding:utf-8 -*-

"""
 Implement strStr().

Returns the index of the first occurrence of needle in haystack,

 or -1 if needle is not part of haystack.
"""

# python中str的find()函数功能
class Solution_1(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ans = haystack.find(needle)    # 等同于str的find()函数功能
        return(ans)

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if (not haystack) and needle:
            return(-1)    # haystack为空，needle不为空，返回-1
        if not needle:
            return(0)    # needle为空，返回''

        # haystack和needle均不为空时
        if len(needle) > len(haystack):
            return(-1)
        length = len(needle)
        for i in range(0,len(haystack)):
            comp = haystack[i:i + length]    # 截取与needle等长的字符串，然后与needle对比
            if comp == needle:
                return(i)
        return(-1)


if __name__ == '__main__':
    solution = Solution()
    haystack = 'a'
    needle = 'a'
    ans = solution.strStr(haystack,needle)
    print(ans)