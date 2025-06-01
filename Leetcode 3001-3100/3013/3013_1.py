# Leetcode 3013: Divide an Array Into Subarrays With Minimum Cost II
# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/
# Solved on 1st of June, 2025
import heapq
from collections import Counter


class Solution:
    def minimumCost(self, nums: list[int], k: int, dist: int) -> int:
        """
        Calculates the minimum cost to divide the array into k subarrays.

        The cost is defined as the sum of the first element of the array (nums[0])
        and the first elements of the k-1 subsequent subarrays. The first element
        of the i-th subsequent subarray (for i from 2 to k) must be located at an
        index j such that its index is at most `dist` away from the index of the
        first element of the (i-1)-th subsequent subarray.

        Args:
            nums: The input list of integers.
            k: The number of subarrays to divide the array into.
            dist: The maximum allowed distance between the first elements of consecutive subsequent subarrays.

        Returns:
            The minimum possible cost.
        """
        n = len(nums)
        # Number of elements s_2, ..., s_{k - 1} to choose
        m = k - 2

        # Constraints: 3 <= k <= n imply m = k - 2 >= 1.
        # Special handling for m < 0 or m = 0 is robust but not strictly needed by these constraints.
        if m < 0:   # k = 1. This case implies n = 1, k = 1 from constraints. Cost is nums[0].
            return nums[0]
        if m == 0:
            minS1Cost = float('inf')
            for i in range(1, n):
                minS1Cost = min(minS1Cost, nums[i])
            return nums[0] + minS1Cost

        smalls = []
        larges = []

        currentSumSmalls = 0
        smallsActualSize = 0
        largesActualSize = 0
        pendingRemoval = Counter()

        def getTopSmalls():
            while smalls and pendingRemoval[(-smalls[0][0], -smalls[0][1])] > 0:
                item = (-smalls[0][0], -smalls[0][1])
                pendingRemoval[item] -= 1
                heapq.heappop(smalls)
            if not smalls:
                return (float('-inf'), float('-inf'))
            return (-smalls[0][0], -smalls[0][1])

        def getTopLarges():
            while larges and pendingRemoval[larges[0]] > 0:
                item = larges[0]
                pendingRemoval[item] -= 1
                heapq.heappop(larges)
            if not larges:
                return float('inf'), float('inf')
            return larges[0]

        def popTopSmalls():
            itemPopped = None
            while smalls:
                rawItemFromHeap = heapq.heappop(smalls)
                itemPopped = (-rawItemFromHeap[0], -rawItemFromHeap[1])
                if pendingRemoval[itemPopped] > 0:
                    pendingRemoval[itemPopped] -= 1; itemPopped = None
                else:
                    break
            return itemPopped

        def popTopLarges():
            itemPopped = None
            while larges:
                itemPopped = heapq.heappop(larges)
                if pendingRemoval[itemPopped] > 0:
                    pendingRemoval[itemPopped] -= 1; itemPopped = None
                else:
                    break
            return itemPopped

        def balanceHeaps():
            nonlocal currentSumSmalls, smallsActualSize, largesActualSize

            # Ensure smalls has at most m elements; move excess to larges
            while smallsActualSize > m:
                itemToMove = popTopSmalls()
                if itemToMove is None:
                    break
                currentSumSmalls -= itemToMove[0]
                smallsActualSize -= 1
                heapq.heappush(larges, itemToMove)
                largesActualSize += 1

            # Ensure smalls has m elements if possible (move from larges)
            while smallsActualSize < m and largesActualSize > 0:
                itemToMove = popTopLarges()
                if itemToMove is None:
                    break
                largesActualSize -= 1
                heapq.heappush(smalls, (-itemToMove[0], -itemToMove[1]))
                currentSumSmalls += itemToMove[0]
                smallsActualSize += 1

            # Ensure patitioning property: top_smalls <= top_larges (value-wise)
            if smallsActualSize > 0 and largesActualSize > 0:
                topSitem = getTopSmalls()
                topLitem = getTopLarges()

                if topSitem > topLitem:
                    sItem = popTopSmalls()
                    lItem = popTopLarges()

                    if sItem is not None:
                        heapq.heappush(larges, sItem)
                        currentSumSmalls -= sItem[0]
                        smallsActualSize -= 1; largesActualSize += 1

                    if lItem is not None:
                        heapq.heappush(smalls, (-lItem[0], -lItem[1]))
                        currentSumSmalls += lItem[0]
                        largesActualSize -= 1; smallsActualSize += 1

        def addElement(val, originalIdx):
            nonlocal currentSumSmalls, smallsActualSize, largesActualSize
            itemToAdd = (val, originalIdx)
            smallsBoundaryItem = getTopSmalls()

            if itemToAdd <= smallsBoundaryItem or smallsActualSize < m:
                heapq.heappush(smalls, (-itemToAdd[0], -itemToAdd[1]))
                currentSumSmalls += itemToAdd[0]
                smallsActualSize += 1
            else:
                heapq.heappush(larges, itemToAdd)
                largesActualSize += 1
            balanceHeaps()

        def removeElement(val, originalIdx):
            nonlocal currentSumSmalls, smallsActualSize, largesActualSize
            itemToRemove = (val, originalIdx)

            smallsBoundaryItem = getTopSmalls()

            if itemToRemove <= smallsBoundaryItem:
                currentSumSmalls -= itemToRemove[0]
                smallsActualSize -= 1
            else:
                largesActualSize -= 1

            pendingRemoval[itemToRemove] += 1
            balanceHeaps()

        ans = float('inf')

        firstS1Idx = 1

        winStartCandidateIdx = firstS1Idx + 1
        winEndCandidateIdx = min(n - 1, firstS1Idx + dist)

        for j_idx in range(winStartCandidateIdx, winEndCandidateIdx + 1):
            addElement(nums[j_idx], j_idx)

        for s1_idx in range(1, n - m):
            currentS1Cost = nums[s1_idx]

            if smallsActualSize == m:
                ans = min(ans, nums[0] + currentS1Cost + currentSumSmalls)

            if s1_idx == n - m - 1:
                break

            # Slide window: element at (current s1Idx) + 1 leaves candidate set
            idxLeavingWindow = s1_idx + 1
            removeElement(nums[idxLeavingWindow], idxLeavingWindow)

            # Element at (next s1Idx) + dist enters candidate set. Next s1idx is (current s1Idx) + 1.
            idxEnteringWindow = (s1_idx + 1) + dist
            if idxEnteringWindow < n:
                addElement(nums[idxEnteringWindow], idxEnteringWindow)

        # Problem constraints should ensure ans is updated from inf.
        return ans