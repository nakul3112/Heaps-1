# Time Complexity:
# O(nklogk) , n = avg no. of elements in the linked list, k = no. of linked lists

# Space Complexity:  
# O(k),  k elements in the heap, meaning at a time, we take 1 element from each of the "k linkedlists    

# Approach: 
# Heap, Use the min heap.


import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        
        pq = []    # Heap
        dummy = ListNode(-1)
        curr = dummy

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(pq, (lists[i].val, i))
                lists[i] = lists[i].next

        while pq:
            val, i = heapq.heappop(pq)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[i]:
                heapq.heappush(pq, (lists[i].val, i))
                lists[i] = lists[i].next
        
        return dummy.next