# Leetcode 3569: Maximize Count of Distinct Primes After Split
# https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/
# Solved on 1st of April, 2026
import heapq
from collections import defaultdict

maxVal = 100000
isPrimeArr = [True] * (maxVal + 1)
isPrimeArr[0] = False
isPrimeArr[1] = False
for i in range(2, int(maxVal ** 0.5) + 1):
    if isPrimeArr[i]:
        for j in range(i * i, maxVal + 1, i):
            isPrimeArr[j] = False


class Solution:
    def maximumCount(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        """
        Calculates the maximum number of distinct primes across two subarrays after splitting nums at any index,
        processing multiple point-update queries.

        :param nums: List of integers to be split.
        :param queries: List of [index, value] pairs representing updates to nums.
        :return: A list of integers where each element is the maximum distinct prime count for that query.
        """
        n = len(nums)
        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def addRange(node, start, end, l, r, val):
            if l <= start and end <= r:
                tree[node] += val
                lazy[node] += val
                return
            mid = (start + end) // 2
            if lazy[node] != 0:
                tree[2 * node] += lazy[node]
                lazy[2 * node] += lazy[node]
                tree[2 * node + 1] += lazy[node]
                lazy[2 * node + 1] += lazy[node]
                lazy[node] = 0
            if l <= mid:
                addRange(2 * node, start, mid, l, r, val)
            if r > mid:
                addRange(2 * node + 1, mid + 1, end, l, r, val)
            tree[node] = max(tree[2 * node], tree[2 * node + 1])

        minHeaps = defaultdict(list)
        maxHeaps = defaultdict(list)
        primeFreq = defaultdict(int)
        activeIntervals = {}
        activePrimesCount = 0

        def getFirstIdx(p):
            while minHeaps[p]:
                idx = minHeaps[p][0]
                if nums[idx] == p:
                    return idx
                heapq.heappop(minHeaps[p])
            return None

        def getLastIdx(p):
            while maxHeaps[p]:
                idx = -maxHeaps[p][0]
                if nums[idx] == p:
                    return idx
                heapq.heappop(maxHeaps[p])
            return None

        def updatePrimeInterval(p):
            if p in activeIntervals:
                l, r = activeIntervals[p]
                addRange(1, 1, n - 1, l, r, -1)
                del activeIntervals[p]
            firstIdx = getFirstIdx(p)
            lastIdx = getLastIdx(p)
            if firstIdx is not None and firstIdx < lastIdx:
                l = firstIdx + 1
                r = lastIdx
                addRange(1, 1, n - 1, l, r, 1)
                activeIntervals[p] = (l, r)

        for idx, val in enumerate(nums):
            if isPrimeArr[val]:
                if primeFreq[val] == 0:
                    activePrimesCount += 1
                primeFreq[val] += 1
                heapq.heappush(minHeaps[val], idx)
                heapq.heappush(maxHeaps[val], -idx)

        for p in list(primeFreq.keys()):
            updatePrimeInterval(p)

        ans = []
        for idx, val in queries:
            oldVal = nums[idx]
            if oldVal == val:
                ans.append(activePrimesCount + tree[1])
                continue

            nums[idx] = val

            if isPrimeArr[oldVal]:
                primeFreq[oldVal] -= 1
                if primeFreq[oldVal] == 0:
                    activePrimesCount -= 1
                updatePrimeInterval(oldVal)

            if isPrimeArr[val]:
                if primeFreq[val] == 0:
                    activePrimesCount += 1
                primeFreq[val] += 1
                heapq.heappush(minHeaps[val], idx)
                heapq.heappush(maxHeaps[val], -idx)
                updatePrimeInterval(val)

            ans.append(activePrimesCount + tree[1])

        return ans