#-*- coding:utf-8 -*-

"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        head_node = ListNode(0)    # 定义一个链表节点，next指向head
        head_node.next = head

        first_node = head_node
        end_node = head_node

        for i in range(n):
            end_node = end_node.next    # 将end_node依次后移n位
        while end_node.next:
            first_node = first_node.next
            end_node = end_node.next    # 将end_node移到最后一个节点上，此时first_node.next指向的节点，即为需要删除的节点

        delete_node = first_node.next
        first_node.next = delete_node.next
        del(delete_node)    # 删去first_node指向的节点

        return(head_node.next)
