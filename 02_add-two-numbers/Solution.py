# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = l1
        second = l2
        
        result = ListNode(0)
        head = result
        carryover = 0
        
        
        while first is not None or second is not None:
            if first is None:
                first = ListNode(0)
            if second is None:
                second = ListNode(0)
                
            s = first.val + second.val + carryover
            carryover = math.floor(s / 10)
            v = s % 10
            
            result.next = ListNode(v)
            
            first = first.next
            second = second.next
            result = result.next
        if carryover != 0:
            result.next = ListNode(carryover)
            
        return head.next
            
        