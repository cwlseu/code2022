from heapq import heapify


class Solution:
    def max_heapify(self, heap, root, heap_len):
        p = root
        while p * 2 + 1 < heap_len:
            # 找到当前节点的左右孩子节点
            l, r = p * 2 + 1, p * 2 + 2
            # 找到孩子节点中较大的节点位置
            if heap_len <= r or heap[r] < heap[l]:
                nex = l
            else:
                nex = r
            # 如果大孩子节点比当前节点值大，那么当前节点与孩子节点进行交换
            if heap[p] < heap[nex]:
                heap[p], heap[nex] = heap[nex], heap[p]
                p = nex
            else:
                break
    def min_heapify(self, heap, root, heap_len):
        p = root
        while p*2+1 < heap_len:
            l, r = p*2 + 1, p*2 + 2
            if heap_len <= r or heap[r] > heap[l]:
                nex = l
            else:
                nex = r
            if heap[p] > heap[nex]:
                heap[p], heap[nex] = heap[nex], heap[p]
                p = nex
            else:
                break

    def build_heap(self, heap):
        for i in range(len(heap) - 1, -1, -1):
            self.max_heapify(heap, i, len(heap))

    def heap_sort(self, nums):
        self.build_heap(nums)
        for i in range(len(nums) - 1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.max_heapify(nums, 0, i)

    def sortArray(self, nums):
        self.heap_sort(nums)
        return nums

    def sortArray_min(self, nums):
        n = len(nums)
        for i in range(n-1, -1, -1):
            self.min_heapify(nums, i, n)
        for i in range(n-1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.min_heapify(nums, 0, i)
        return nums

s = Solution()
unsorted_arr = [7,8,9,10, 1,2,4,5]
print(unsorted_arr)
res = s.sortArray(unsorted_arr)
print(res)
res = s.sortArray_min(unsorted_arr)
print(unsorted_arr)
print(res)

from collections import heapq
heapq.heappushpop()
