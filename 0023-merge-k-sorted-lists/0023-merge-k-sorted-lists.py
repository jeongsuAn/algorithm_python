# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from itertools import count

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        rand_num = count()

        for i in range(len(lists)):
            while lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, next(rand_num) , lists[i]))
                lists[i] = lists[i].next

        result = None
        cur = None
        
        while heap:
            if result is None:
                result = heapq.heappop(heap)[2]
                cur = result
            else:
                cur.next = heapq.heappop(heap)[2]
                cur = cur.next

        return result
