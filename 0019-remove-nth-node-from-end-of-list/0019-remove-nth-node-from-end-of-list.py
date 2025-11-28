# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        # Create a dummy node to simplify edge cases (like removing the first node)
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove the nth node
        slow.next = slow.next.next

        return dummy.next


# Helper functions to test the code
def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head

def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)


# Example usage
head = create_linked_list([1, 2, 3, 4, 5])
n = 2
result = Solution().removeNthFromEnd(head, n)
print_linked_list(result)      