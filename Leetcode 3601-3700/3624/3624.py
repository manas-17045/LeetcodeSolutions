# Leetcode 3624: Number of Integers With Popcount-Depth Equal to K II
# https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/
# Solved on 19th of December, 2025
class Solution:
    def popcountDepth(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        """
        Calculates the number of integers with a specific popcount-depth within given ranges and handles updates.

        Args:
            nums: A list of integers.
            queries: A list of queries. Each query can be either a type 1 query [1, l, r, k] or a type 2 query [2, idx, val].
        Returns:
            A list of integers, where each element is the answer to a type 1 query.
        """
        n = len(nums)
        maxDepth = 5
        trees = [[0] * (n + 1) for _ in range(maxDepth + 1)]
        currentDepths = [0] * n

        def getDepth(num):
            depth = 0
            while num != 1:
                num = bin(num).count('1')
                depth += 1
            return depth

        def update(treeIdx, idx, delta):
            idx += 1
            while idx <= n:
                trees[treeIdx][idx] += delta
                idx += idx & (-idx)

        def query(treeIdx, idx):
            idx += 1
            total = 0
            while idx > 0:
                total += trees[treeIdx][idx]
                idx -= idx & (-idx)
            return total

        for i in range(n):
            d = getDepth(nums[i])
            currentDepths[i] = d
            if d <= maxDepth:
                update(d, i, 1)

        ans = []
        for q in queries:
            if q[0] == 1:
                l, r, k = q[1], q[2], q[3]
                if k <= maxDepth:
                    count = query(k, r) - query(k, l - 1)
                    ans.append(count)
                else:
                    ans.append(0)
            else:
                idx, val = q[1], q[2]
                oldDepth = currentDepths[idx]
                newDepth = getDepth(val)

                if oldDepth == newDepth:
                    nums[idx] = val
                    continue

                if oldDepth <= maxDepth:
                    update(oldDepth, idx, -1)
                if newDepth <= maxDepth:
                    update(newDepth, idx, 1)

                currentDepths[idx] = newDepth
                nums[idx] = val

        return ans