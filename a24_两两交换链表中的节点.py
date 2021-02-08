'''
* @File: a24_两两交换链表中的节点.py
* @Author: CSY
* @Date: 2019/7/27 - 11:26
'''
"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         p = head
#         while p is not None and p.next is not None: #前后都存在
#             tmp = p.val  #前一个值a,给t,
#             p.val = p.next.val # 后一个值b,给a
#             p.next.val = tmp #t再给b,
#             p = p.next.next
#         return head

# 给定 1->2->3->4, 你应该返回 2->1->4->3.