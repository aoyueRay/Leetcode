#-*- coding:utf-8 -*-

"""
Merge k sorted linked lists and return it as one sorted list.

Analyze and describe its complexity.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 将k个链表，通过拆分的方式，递归调用自身，最后变成两个链表的排序
# 即两两链表排序后，最后组成新的链表
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return(None)    # 为空的情况
        if len(lists) == 1:
            return(lists[0])    # 长度为1的情况

        mid = len(lists) / 2    # 拆分为两个链表再操作
        left = self.mergeKLists(lists[:mid])    #递归调用
        right = self.mergeKLists(lists[mid:])    # 递归调用

        head_node = ListNode(0)
        temp = head_node

        while left or right:    # left或right有一个不为空时
            if (not right) or (left and left.val < right.val):
                temp.next = left    # right为空，或者left.val小于right.val时，temp指向left
                left = left.next    # left后移一位
            else:
                temp.next = right
                right = right.next    # 否则temp指向right，right后移一位
            temp = temp.next    # temp后移一位
        return(head_node.next)