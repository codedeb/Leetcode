class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = head = ListNode(0)

        # checking edge conditions
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        while (l1 and l2):
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 or l2

        return head.next
