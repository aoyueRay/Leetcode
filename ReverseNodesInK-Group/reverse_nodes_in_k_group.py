#-*- coding:utf-8 -*-

"""
 Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 定义指针，移动k个位置，截断链表，将截断部分逆序处理
# 逆序后再重新接上，重置指针，重复上一步的处理
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        head_node = ListNode(0)    # 定义头结点
        head_node.next = head
        first_node = head_node
        last_node = head_node
        n = 1    # 初始化，移动的次数

        while last_node.next:
            last_node = last_node.next    # 将last结点后移k个位置
            if n == k:    # last结点移动k个位置后
                next_node = last_node.next
                last_node.next = None    # 将链表切断

                # 将first为首的链表逆序
                last_node = first_node.next
                while last_node.next:
                    temp_node = last_node.next
                    last_node.next = temp_node.next    # 先断倒数第二个结点
                    temp_node.next = first_node.next    # 再断最后一个结点
                    first_node.next = temp_node    # 再处理第一个结点
                last_node.next = next_node    # 将逆序后的链表与剩余链表连接起来
                first_node = last_node    # 移动头结点指针的位置
                n = 0    # 重置移动次数
            n += 1
        return(head_node.next)
