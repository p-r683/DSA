class Solution:
    def removeNthFromEnd(self, head, n):
        curr = head
        length = 0

        # Find length
        while curr is not None:
            length += 1
            curr = curr.next

        # If removing the first node
        if n == length:
            return head.next

        # Move to node BEFORE the one to delete
        curr = head
        count=1
        node =length -n
        while count<node:
            curr = curr.next
            count+=1
        # Delete next node
        curr.next = curr.next.next

        return head