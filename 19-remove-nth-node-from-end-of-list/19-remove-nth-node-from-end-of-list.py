# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:        

        start = head
        end = head
        prev = None
        
        for i in range (n-1):
            end = end.next
            
        if end.next is None:
            return head.next
        
        while end.next:
            prev = start
            end = end.next
            start = start.next 
            
        #delete the node
        prev.next = start.next 
        start.next = None
        return head
            
        
        
        
                
        