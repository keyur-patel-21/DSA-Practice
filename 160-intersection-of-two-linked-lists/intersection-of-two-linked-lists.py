# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        curA, curB = headA, headB
        countA, countB = 0, 0

        while curA:
            curA = curA.next
            countA += 1

        while curB:
            curB = curB.next
            countB += 1
        
        curA, curB = headA, headB

        while countA > countB:
            curA = curA.next
            countA -= 1

        while countB > countA:
            curB = curB.next
            countB -= 1

        while curA != curB:
            curA = curA.next
            curB = curB.next

        return curA