from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev = head
        curr = head.next
        curr_idx = 1
        
        first_critical_idx = -1
        prev_critical_idx = -1
        min_dist = float('inf')
        
        while curr and curr.next:
            nxt = curr.next
            
            # Check if curr is a local minima or local maxima
            is_minima = curr.val < prev.val and curr.val < nxt.val
            is_maxima = curr.val > prev.val and curr.val > nxt.val
            
            if is_minima or is_maxima:
                if first_critical_idx == -1:
                    first_critical_idx = curr_idx
                else:
                    min_dist = min(min_dist, curr_idx - prev_critical_idx)
                prev_critical_idx = curr_idx
            
            prev = curr
            curr = nxt
            curr_idx += 1
        
        # If less than 2 critical points found
        if first_critical_idx == -1 or prev_critical_idx == first_critical_idx:
            return [-1, -1]
        
        max_dist = prev_critical_idx - first_critical_idx
        return [int(min_dist), max_dist]