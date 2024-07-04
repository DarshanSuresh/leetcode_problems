# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        # Initialize a dummy node to help with the new list construction
        dummy = ListNode(0)
        current = dummy
        sum_between_zeros = 0
        
        # Iterate through the linked list starting from the next node of the head
        node = head.next
        while node:
            if node.val == 0:
                # When we encounter a zero, create a new node with the sum and reset the sum
                current.next = ListNode(sum_between_zeros)
                current = current.next
                sum_between_zeros = 0
            else:
                # Add the value of the current node to the sum
                sum_between_zeros += node.val
            # Move to the next node in the list
            node = node.next
        
        return dummy.next
