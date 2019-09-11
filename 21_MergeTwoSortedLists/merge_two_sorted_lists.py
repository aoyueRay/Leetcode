#-*- coding:utf-8 -*-

"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return(None)    # l1和l2均为空时，返回None

        head_node = ListNode(0)
        answer = head_node

        # l1 和 l2 都存在时，比较两者值的大小。
        # 若l1小于l2,则answer.next指向l1,l1后移
        # 若l2小于l1,则answer.next指向l2,l2后移
        while l1 and l2:
            if l1.val <= l2.val:
                answer.next = l1
                l1 = l1.next
            else:
                answer.next = l2
                l2 = l2.next
            answer = answer.next    # answer后移
        answer.next = l1 or l2    # l1或l2其中一个为空时，answer.next指向另一个

        return(head_node.next)