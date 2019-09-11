#-*- coding:utf-8 -*-
"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # l1 或 l2 有一个为空链表的处理
        if not l1:
            return(l2)
        if not l2:
            return(l1)
        dummy = ListNode(0)    # 初始化一个空链表
        ans = dummy    # 初始结果是一个空链表
        carry = 0    # 进位

        # l1 和 l2 都有值时
        while l1 and l2:
            value = l1.val + l2.val + carry
            ans.next = ListNode(value % 10)    # 定义一个链表节点

            carry = value / 10
            l1 = l1.next    # 获取下一个链表节点
            l2 = l2.next    # 获取下一个链表节点
            ans = ans.next    # 获取下一个链表节点

        # l1 有值而 l2 为空时
        if l1:
            while l1:
                value = l1.val + carry
                ans.next = ListNode(value % 10)
                carry = value / 10
                l1 = l1.next
                ans = ans.next

        # l2 有值而 l1 为空时
        if l2:
            while l2:
                value = l2.val + carry
                ans.next = ListNode(value % 10)
                carry = value / 10
                l2 = l2.next
                ans = ans.next

        # 最后一个节点相加有进位时的处理
        if carry == 1:
            ans.next = ListNode(carry)
        return(dummy.next)


solution = Solution()
l1 = [2,4,3]
l2 = [5,6,4]
asns = solution.addTwoNumbers(l1,l2)
print(ans)