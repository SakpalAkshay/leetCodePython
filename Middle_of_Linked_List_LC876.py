class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, count = head, 0
        while curr:
            count+=1
            curr = curr.next
        trav = count//2
        for i in range(trav):
            head = head.next
        return head
