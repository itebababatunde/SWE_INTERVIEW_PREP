# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return self.check_arr(arr)
    
            
    def check_arr(self, arr):
        
        if len(arr) == 0 or len(arr)==1:
            return True

        if arr[0] == arr[-1]:
            arr.pop(0)
            arr.pop(-1)
            return self.check_arr(arr)
        else: 
            return False
        return True