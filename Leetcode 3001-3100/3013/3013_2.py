# Leetcode 3013: Divide an Array Into Subarrays With Minimum Cost II
# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/
# Solved on 1st of June, 2025
import heapq


class Solution:
    def minimumCost(self, nums: list[int], k: int, dist: int) -> int:
        """
        Calculates the minimum cost to select k elements from the array `nums`
        such that the first element is `nums[0]` and the remaining k-1 elements
        are chosen from a window of size `dist + 1` that slides from index 1
        to n-1.

        The cost is the sum of the selected elements.

        Args:
            nums: A list of integers.
            k: The number of elements to select.
            dist: The maximum distance between consecutive selected elements (excluding the first).

        Returns:
            The minimum possible cost.
        """
        n = len(nums)
        # Base case
        if k == 1:
            return nums[0]

        INF = 10**18

        selectedMaxHeap = []
        candidatesMinHeap = []
        delayedSel = {}
        delayedCan = {}

        sizeSel = 0
        sizeCan = 0
        sumSel = 0

        def prune(heap: list[int], delayed: dict):
            while heap:
                v = heap[0]
                actual = (-v) if (heap is selectedMaxHeap) else v
                if delayed.get(actual, 0) > 0:
                    heapq.heappop(heap)
                    delayed[actual] -= 1
                else:
                    break

        def topSelected() -> int:
            prune(selectedMaxHeap, delayedSel)
            if not selectedMaxHeap:
                return None
            return -selectedMaxHeap[0]

        def topCandidate() -> int:
            prune(candidatesMinHeap, delayedCan)
            if not candidatesMinHeap:
                return None
            return candidatesMinHeap[0]

        def addValue(x: int):
            nonlocal sizeSel, sizeCan, sumSel

            if sizeSel < (k - 1):
                heapq.heappush(selectedMaxHeap, -x)
                sumSel += x
                sizeSel += 1
            else:
                largestInSel = topSelected()
                if largestInSel is not None and x < largestInSel:
                    heapq.heappop(selectedMaxHeap)
                    sumSel -= largestInSel
                    sizeSel -= 1

                    heapq.heappush(candidatesMinHeap, largestInSel)
                    sizeCan += 1

                    heapq.heappush(selectedMaxHeap, -x)
                    sumSel += x
                    sizeSel += 1
                else:
                    heapq.heappush(candidatesMinHeap, x)
                    sizeCan += 1

        def removeValue(y: int):
            nonlocal sizeSel, sizeCan, sumSel

            largestInSel = topSelected()
            if largestInSel is not None and y <= largestInSel:
                sumSel -= y
                sizeSel -= 1
                delayedSel[y] = delayedSel.get(y, 0) + 1

                # Refill one candidate from candidatesMinHeap (the smallest there) into selectedMaxHeap
                smallestInCan = topCandidate()
                if smallestInCan is not None:
                    heapq.heappop(candidatesMinHeap)
                    sizeCan -= 1

                    heapq.heappush(selectedMaxHeap, -smallestInCan)
                    sumSel += smallestInCan
                    sizeSel += 1
            else:
                # y lies in candidatesMinHeap
                delayedCan[y] = delayedCan.get(y, 0) + 1
                sizeCan -= 1

        ans = INF

        # Slide r from 1 to (n - 1) over the array nums[i...(n - 1)].
        for r in range(1, n):
            # Add nums[r] to our two-heap structure
            addValue(nums[r])

            if r - dist - 1 >= 1:
                removeValue(nums[r - dist - 1])

            # Compute the current window size = r - max(1, r - dist) + 1.
            leftIndex = max(1, r - dist)
            windowSize = (r - leftIndex + 1)

            # Only if that window has at least (k - 1) elements, can we pick (k - 1) starts.
            if windowSize >= (k - 1):
                currentCost = nums[0] + sumSel
                if currentCost < ans:
                    ans = currentCost

        return ans