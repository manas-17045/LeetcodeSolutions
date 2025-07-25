# Leetcode 2916: Subarrays Distinct Element Sum of Squares II
# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/
# Solved on 25th of July, 2025
class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        """
        Calculates the sum of squares of distinct element counts for all subarrays.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            int: The total sum of squares of distinct element counts modulo 10^9 + 7.
        """
        n = len(nums)
        mod = 10 ** 9 + 7

        sumVal = [0] * (4 * n)
        sumSqVal = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def push(node, start, end):
            if lazy[node] == 0:
                return

            val = lazy[node]

            if start != end:
                mid = (start + end) // 2
                leftNode = 2 * node
                rightNode = 2 * node + 1
                lenLeft = mid - start + 1
                lenRight = end - mid

                sumSqVal[leftNode] = (sumSqVal[leftNode] + 2 * val * sumVal[leftNode] + lenLeft * val * val) % mod
                sumVal[leftNode] = (sumVal[leftNode] + lenLeft * val) % mod
                lazy[leftNode] = (lazy[leftNode] + val) % mod

                sumSqVal[rightNode] = (sumSqVal[rightNode] + 2 * val * sumVal[rightNode] + lenRight * val * val) % mod
                sumVal[rightNode] = (sumVal[rightNode] + lenRight * val) % mod
                lazy[rightNode] = (lazy[rightNode] + val) % mod

            lazy[node] = 0

        def update(node, start, end, l, r, val):
            if start > r or end < l:
                return

            if l <= start and end <= r:
                length = end - start + 1
                sumSqVal[node] = (sumSqVal[node] + 2 * val * sumVal[node] + length * val * val) % mod
                sumVal[node] = (sumVal[node] + length * val) % mod
                lazy[node] = (lazy[node] + val) % mod
                return

            push(node, start, end)
            mid = (start + end) // 2
            leftNode = 2 * node
            rightNode = 2 * node + 1
            update(leftNode, start, mid, l, r, val)
            update(rightNode, mid + 1, end, l, r, val)

            sumVal[node] = (sumVal[leftNode] + sumVal[rightNode]) % mod
            sumSqVal[node] = (sumSqVal[leftNode] + sumSqVal[rightNode]) % mod

        totalSum = 0
        lastSeen = {}

        for j in range(n):
            num = nums[j]
            p = lastSeen.get(num, -1)

            update(1, 0, n - 1, p + 1, j, 1)

            currentSumSq = sumSqVal[1]
            totalSum = (totalSum + currentSumSq) % mod

            lastSeen[num] = j

        return totalSum