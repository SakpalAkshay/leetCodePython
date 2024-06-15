class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        fast = head
        slow = None

        while fast:
            if fast.val ==val:
                if slow:
                    slow.next = fast.next
                else:
                    head = fast.next
                fast = fast.next
            else:
                slow = fast
                fast = fast.next
        return head
