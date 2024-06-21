import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val

        data = []
        heapq.heapify(data)
        for i in lists:
            if i:
                heapq.heappush(data, i)

        dummy_head = ListNode(10**-5)
        current = dummy_head
        while data:
            el = heapq.heappop(data)
            current.next = el
            if el.next:
                heapq.heappush(data, el.next)
            current = current.next
        return dummy_head.next


        
