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
        
    def removeElements2(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head==None:return head   
        while head and head.val==val:
            head=head.next
        dummy=previous=head
        while head:
            if head.val==val:
                previous.next=head.next
                head=head.next
            else: 
                previous=head
                head=head.next

        return dummy
