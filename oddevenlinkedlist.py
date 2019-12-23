# class ListNode:
#     def __init__(self, x):
#     self.val = x
#     self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        odd = head  # head postion is odd
        even = head.next  # head.next possition is even
        evenHead = even  # to join oddtail to evenHead

        while even and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenHead
        return head
