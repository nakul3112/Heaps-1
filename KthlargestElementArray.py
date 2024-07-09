# Time Complexity:
# O(nlogk) , n = no. of elements in the array

# Space Complexity:  
# O(k),   k is given kth largest number to find     

# Approach: 
# Heap, Use the min heap, while limiting the capacity of min heap elements to "k"

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or len(nums)==0:
            return -1

        minHeap = []    # Initiate a MinHeap (priorityQueue)

        for i in range(0,len(nums)):
            heapq.heappush(minHeap, nums[i])  #insert element into the heappush
            if (len(minHeap) > k):
                heapq.heappop(minHeap)       # remove the smallest element from the heap
        
        # at this point, the minHeap contains only the k largest values,
        # so return the heap's top element
        return minHeap[0]     