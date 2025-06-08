# Leetcode 3410: Maximize Subarray Sum After Removing All Occurrences of One Element
# https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/
# Solved on 8th of June, 2025

class Solution:
    def maxSubarraySum(self, nums: list[int]) -> int:
        """
        Given an array of integers nums, you are allowed to remove all occurrences of one element.
        Return the maximum subarray sum of the remaining elements.

        This problem can be solved by considering each unique element in the array.
        For each unique element, we remove all its occurrences and then find the maximum
        subarray sum of the remaining elements. The overall maximum subarray sum among
        all possible removals is the answer.

        To efficiently find the maximum subarray sum of the remaining elements after
        removing occurrences of a specific element, we can use a segment tree.
        The segment tree stores information about subarray sums (total sum, max prefix sum,
        max suffix sum, and max subarray sum) for ranges of the original array.
        When an element is removed, the remaining array is a concatenation of segments
        from the original array. We can query the segment tree for each segment and combine
        the results to find the maximum subarray sum of the remaining elements.
        """
        n = len(nums)
        negInf = -float('inf')

        def kadane(arr):
            if not arr:
                return negInf

            maxSoFar = negInf
            currentMax = negInf

            for x in arr:
                currentMax = max(x, currentMax + x)
                maxSoFar = max(maxSoFar, currentMax)

            return maxSoFar

        maxAns = kadane(nums)

        locsMap = {}
        for i, num in enumerate(nums):
            if num not in locsMap:
                locsMap[num] = []
            locsMap[num].append(i)

        identityNode = [0, negInf, negInf, negInf]
        tree = [identityNode] * (4 * n)

        def combine(leftNode, rightNode):
            if leftNode == identityNode:
                return rightNode
            if rightNode == identityNode:
                return leftNode

            totalSum = leftNode[0] + rightNode[0]
            maxPrefix = max(leftNode[1], leftNode[0] + rightNode[1])
            maxSuffix = max(rightNode[2], rightNode[0] + leftNode[2])
            maxSubarray = max(leftNode[3], rightNode[3], leftNode[2] + rightNode[1])

            return [totalSum, maxPrefix, maxSuffix, maxSubarray]

        def build(nodeIndex, rangeLeft, rangeRight):
            if rangeLeft == rangeRight:
                val = nums[rangeLeft]
                tree[nodeIndex] = [val, val, val, val]
                return

            mid = (rangeLeft + rangeRight) // 2
            build(2 * nodeIndex, rangeLeft, mid)
            build(2 * nodeIndex + 1, mid + 1, rangeRight)
            tree[nodeIndex] = combine(tree[2 * nodeIndex], tree[2 * nodeIndex + 1])

        def query(nodeIndex, rangeLeft, rangeRight, queryLeft, queryRight):
            if rangeLeft > queryRight or rangeRight < queryLeft:
                return identityNode

            if queryLeft <= rangeLeft and rangeRight <= queryRight:
                return tree[nodeIndex]

            mid = (rangeLeft + rangeRight) // 2
            leftRes = query(2 * nodeIndex, rangeLeft, mid, queryLeft, queryRight)
            rightRes = query(2 * nodeIndex + 1, mid + 1, rangeRight, queryLeft, queryRight)

            return combine(leftRes, rightRes)

        if n > 0:
            build(1, 0, (n - 1))

        for v, locs in locsMap.items():
            if len(locs) == n:
                continue

            extendedLocs = [-1] + locs + [n]

            currentRes = identityNode

            for i in range(len(extendedLocs) - 1):
                start = extendedLocs[i] + 1
                end = extendedLocs[i + 1] - 1

                if start <= end:
                    segmentProps = query(1, 0, (n - 1), start, end)
                    currentRes = combine(currentRes, segmentProps)

            if currentRes != identityNode:
                maxAns = max(maxAns, currentRes[3])

        return int(maxAns)