#-*- coding:utf-8 -*-

"""
 Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space.

You may not modify the values in the list, only nodes itself can be changed.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return(None)    # 为空时返回None值

        head_node = ListNode(0)    # 初始化一个头节点，指向head
        head_node.next = head

        first_node = head_node
        last_node = head_node    # 定义两个指针节点

        while last_node.next:
            last_node = last_node.next    # 后一个节点存在时，尾指针后移一位
            if last_node.next:    # 后一个节点存在时，即存在两个可以相互交换的节点，则交换位置
                first_node.next = last_node.next
                last_node.next = first_node.next.next
                first_node.next.next = last_node

                first_node = last_node    # 首指针移动到尾指针处，准备进行下一次判断
        return(head_node.next)
