# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
        return True
        
