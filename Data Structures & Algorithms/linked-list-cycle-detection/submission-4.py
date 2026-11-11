# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # using a data strucutre with O(1) ish lookup

        hashmap = []

        cur = head

        while cur:
            if cur in hashmap:
                return True

            hashmap.append(cur)
            cur = cur.next
        
        return False