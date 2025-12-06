# Leetcode 3721: Longest Balanced Subarray II
# https://leetcode.com/problems/longest-balanced-subarray-ii/
# Solved on 6th of December, 2025
class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        """
        Finds the length of the longest balanced subarray.

        A subarray is balanced if the count of even numbers equals the count of odd numbers.
        :param nums: A list of integers.
        :return: The length of the longest balanced subarray.
        """
        n = len(nums)
        treeMin = [0] * (4 * n)
        treeMax = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def build(node, start, end):
            if start == end:
                treeMin[node] = float('inf')
                treeMax[node] = float('-inf')
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            treeMin[node] = float('inf')
            treeMax[node] = float('-inf')

        def push(node):
            if lazy[node] != 0:
                lazy[2 * node] += lazy[node]
                treeMin[2 * node] += lazy[node]
                treeMax[2 * node] += lazy[node]

                lazy[2 * node + 1] += lazy[node]
                treeMin[2 * node + 1] += lazy[node]
                treeMax[2 * node + 1] += lazy[node]

                lazy[node] = 0

        def updateRange(node, start, end, l, r, val):
            if l > end or r < start:
                return
            if l <= start and end <= r:
                treeMin[node] += val
                treeMax[node] += val
                lazy[node] += val
                return
            push(node)
            mid = (start + end) // 2
            updateRange(2 * node, start, mid, l, r, val)
            updateRange(2 * node + 1, mid + 1, end, l, r, val)
            treeMin[node] = min(treeMin[2 * node], treeMin[2 * node + 1])
            treeMax[node] = max(treeMax[2 * node], treeMax[2 * node + 1])

        def updatePoint(node, start, end, idx, val):
            if start == end:
                treeMin[node] = val
                treeMax[node] = val
                lazy[node] = 0
                return
            push(node)
            mid = (start + end) // 2
            if idx <= mid:
                updatePoint(2 * node, start, mid, idx, val)
            else:
                updatePoint(2 * node + 1, mid + 1, end, idx, val)
            treeMin[node] = min(treeMin[2 * node], treeMin[2 * node + 1])
            treeMax[node] = max(treeMax[2 * node], treeMax[2 * node + 1])

        def query(node, start, end):
            if treeMin[node] > 0 or treeMax[node] < 0:
                return -1
            if start == end:
                return start
            push(node)
            mid = (start + end) // 2
            res = query(2 * node, start, mid)
            if res != -1:
                return res
            return query(2 * node + 1, mid + 1, end)

        build(1, 0, n - 1)
        lastPos = {}
        maxLen = 0

        for i in range(n):
            num = nums[i]
            prev = lastPos.get(num, -1)
            lastPos[num] = i

            updatePoint(1, 0, n - 1, i, 0)

            val = 1 if num % 2 == 0 else -1
            updateRange(1, 0, n - 1, prev + 1, i, val)

            firstIdx = query(1, 0, n - 1)
            if firstIdx != -1:
                maxLen = max(maxLen, i - firstIdx + 1)

        return maxLen