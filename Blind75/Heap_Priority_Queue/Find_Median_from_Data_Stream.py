# Leetcode 295
import heapq
class MedianFinder:

    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []
    def addNum(self, num: int) -> None:
        if self.right_min_heap and num>self.right_min_heap[0]:
            heapq.heappush(self.right_min_heap,num)
        else:
            heapq.heappush(self.left_max_heap,-num)
        if len(self.left_max_heap) > len(self.right_min_heap)+1:
            left_max = -heapq.heappop(self.left_max_heap)
            heapq.heappush(self.right_min_heap,left_max)
        if len(self.right_min_heap) > len(self.left_max_heap)+1:
            right_min = -heapq.heappop(self.right_min_heap)
            heapq.heappush(self.left_max_heap,right_min)
    def findMedian(self) -> float:
        if len(self.left_max_heap)>len(self.right_min_heap):
            return -self.left_max_heap[0]
        elif len(self.right_min_heap)>len(self.left_max_heap):
            return self.right_min_heap[0]
        else:
            return (self.right_min_heap[0]-self.left_max_heap[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
medianFinder =MedianFinder()
medianFinder.addNum(1)    # arr = [1]
medianFinder.addNum(2)    # arr = [1, 2]
print(medianFinder.findMedian()) # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3)    # arr[1, 2, 3]
print(medianFinder.findMedian()) # return 2.0
