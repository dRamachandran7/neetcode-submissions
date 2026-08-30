# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head
        cur = head.next
        next_node = cur.next
        head.next = None

        while cur != None:
            cur.next = head
            head = cur
            cur = next_node
            if next_node == None:
                break
            next_node = next_node.next
        
        return head
        
            
        