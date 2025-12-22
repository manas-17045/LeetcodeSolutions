# Leetcode 3762: Minimum Operations to Equalize Subarrays
# https://leetcode.com/problems/minimum-operations-to-equalize-subarrays/
# Solved on 22nd of December, 2025
class Solution:
    def minOperations(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        """
        Calculates the minimum operations to equalize subarrays for given queries.

        Args:
            nums: A list of integers representing the input array.
            k: An integer representing the divisor for operations.
            queries: A list of lists, where each inner list [l, r] represents a query for the subarray nums[l:r+1].

        Returns:
            A list of integers, where each element is the minimum operations for the corresponding query,
            or -1 if equalization is not possible.
        """
        n = len(nums)
        vals = [x // k for x in nums]
        rems = [x % k for x in nums]

        mismatch = [0] * n
        for i in range(1, n):
            if rems[i] != rems[i - 1]:
                mismatch[i] = 1

        prefixMismatch = [0] * (n + 1)
        for i in range(n):
            prefixMismatch[i + 1] = prefixMismatch[i] + mismatch[i]

        sortedValues = sorted(list(set(vals)))
        rankMap = {val: i for i, val in enumerate(sortedValues)}
        uniqueCount = len(sortedValues)

        leftChildren = []
        rightChildren = []
        counts = []
        sums = []

        def createNode(cnt, totalSum, left=-1, right=-1):
            idx = len(counts)
            counts.append(cnt)
            sums.append(totalSum)
            leftChildren.append(left)
            rightChildren.append(right)
            return idx

        nullNode = createNode(0, 0, 0, 0)
        leftChildren[0] = 0
        rightChildren[0] = 0

        roots = [0] * (n + 1)

        def build(prevNode, l, r, targetRank, val):
            newNode = createNode(counts[prevNode] + 1, sums[prevNode] + val)
            if l == r:
                return newNode

            mid = (l + r) // 2
            if targetRank <= mid:
                newLeft = build(leftChildren[prevNode], l, mid, targetRank, val)
                leftChildren[newNode] = newLeft
                rightChildren[newNode] = rightChildren[prevNode]
            else:
                newRight = build(rightChildren[prevNode], mid + 1, r, targetRank, val)
                leftChildren[newNode] = leftChildren[prevNode]
                rightChildren[newNode] = newRight
            return newNode

        for i in range(n):
            rank = rankMap[vals[i]]
            roots[i + 1] = build(roots[i], 0, uniqueCount - 1, rank, vals[i])

        def getKthRank(nodeL, nodeR, l, r, k):
            if l == r:
                return l
            mid = (l + r) // 2
            countLeft = counts[leftChildren[nodeR]] - counts[leftChildren[nodeL]]
            if k <= countLeft:
                return getKthRank(leftChildren[nodeL], leftChildren[nodeR], l, mid, k)
            else:
                return getKthRank(rightChildren[nodeL], rightChildren[nodeR], mid + 1, r, k - countLeft)

        def getStats(nodeL, nodeR, l, r, limitRank):
            if r <= limitRank:
                return counts[nodeR] - counts[nodeL], sums[nodeR] - sums[nodeL]
            if l > limitRank:
                return 0, 0

            mid = (l + r) // 2
            cnt1, sum1 = getStats(leftChildren[nodeL], leftChildren[nodeR], l, mid, limitRank)
            cnt2, sum2 = getStats(rightChildren[nodeL], rightChildren[nodeR], mid + 1, r, limitRank)
            return cnt1 + cnt2, sum1 + sum2

        results = []
        for l, r in queries:
            if prefixMismatch[r + 1] - prefixMismatch[l + 1] > 0:
                results.append(-1)
                continue

            numElements = r - l + 1
            kth = (numElements + 1) // 2

            medianRank = getKthRank(roots[l], roots[r + 1], 0, uniqueCount - 1, kth)
            medianVal = sortedValues[medianRank]

            cntLeft, sumLeft = getStats(roots[l], roots[r + 1], 0, uniqueCount - 1, medianRank)

            cntTotal = counts[roots[r + 1]] - counts[roots[l]]
            sumTotal = sums[roots[r + 1]] - sums[roots[l]]

            cntRight = cntTotal - cntLeft
            sumRight = sumTotal - sumLeft

            cost = (cntLeft * medianVal - sumLeft) + (sumRight - cntRight * medianVal)
            results.append(cost)

        return results