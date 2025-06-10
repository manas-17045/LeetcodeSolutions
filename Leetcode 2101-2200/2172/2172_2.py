# Leetcode 2172: Maximum AND Sum of Array
# https://leetcode.com/problems/maximum-and-sum-of-array/
# Solved on 10th of June, 2025

class Solution:
    def maximumANDSum(self, nums: list[int], numSlots: int) -> int:
        """
        Calculates the maximum possible bitwise AND sum of elements in `nums`
        when placing them into `numSlots` slots, where each slot can hold at
        most two numbers. The bitwise AND sum is calculated as the sum of
        (nums[i] & slot_index) for each number nums[i] placed in a slot with
        index slot_index.

        This problem is modeled as a maximum weight bipartite matching problem
        and solved using the Hungarian (Kuhn-Munkres) algorithm.

        Args:
            nums: A list of integers.
            numSlots: The number of available slots.
        """
        n = len(nums)
        m = 2 * numSlots
        N = max(n, m)

        # Build weight matrix w[i][j] = nums[i] & slotIndex(j)
        w = [[0] * N for _ in range(N)]
        for i in range(n):
            for j in range(m):
                slot = (j // 2) + 1
                w[i][j] = nums[i] & slot

        # Build cost matrix for minimization: a[i][j] = -w[i][j]
        a = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                a[i][j] = -w[i][j]

        # Hungarian (Kuhn-Munkres) to minimize total cost
        # over an N * N cost matrix a; 1-based indexing inside
        u = [0] * (N + 1)
        v = [0] * (N + 1)
        p = [0] * (N + 1)
        way = [0] * (N + 1)

        for i in range(1, N + 1):
            p[0] = i
            j0 = 0
            minV = [float('inf')] * (N + 1)
            used = [False] * (N + 1)
            while True:
                used[j0] = True
                i0 = p[j0]
                delta = float('inf')
                j1 = 0
                for j in range(1, N + 1):
                    if not used[j]:
                        cur = a[i0 - 1][j - 1] - u[i0] - v[j]
                        if cur < minV[j]:
                            minV[j] = cur
                            way[j] = j0
                        if minV[j] < delta:
                            delta = minV[j]
                            j1 = j

                # Update potentials
                for j in range(N + 1):
                    if used[j]:
                        u[p[j]] += delta
                        v[j] -= delta
                    else:
                        minV[j] -= delta

                j0 = j1
                if p[j0] != 0:
                    continue

                # Augmenting the matching
                while True:
                    j1 = way[j0]
                    p[j0] = p[j1]
                    j0 = j1
                    if j0 == 0:
                        break
                break

        # p[j] = row matched to column j
        # Sum up the corresponding weights for real numbers & real slot-copies
        ans = 0
        for j in range(1, (m + 1)):
            i = p[j]
            if 1 <= i <= n:
                ans += w[i - 1][j - 1]

        return ans