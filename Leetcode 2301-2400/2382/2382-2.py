# Leetcode 2382: Maximum Segment Sum After Removals
# https://leetcode.com/problems/maximum-segment-sum-after-removals/
# Solved on 26th of August, 2025
class Solution:
    def maximumSegmentSum(self, nums: list[int], removeQueries: list[int]) -> list[int]:
        """
        Calculates the maximum segment sum after each removal query.

        Args:
            nums (list[int]): The initial array of numbers.
            removeQueries (list[int]): A list of indices to be removed in order.

        Returns:
            list[int]: A list where each element `ans[i]` is the maximum segment sum
                        after the first `i` elements of `removeQueries` have been removed.
        """
        n = len(nums)
        parent = list(range(n))
        seg_sum = [0] * n
        size = [1] * n
        active = [False] * n

        def find(x: int) -> int:
            # Path compression
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> int:
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return ra
            # Union by size: attach smaller to larger
            if size[ra] < size[rb]:
                ra, rb = rb, ra

            parent[rb] = ra
            size[ra] += size[rb]
            seg_sum[ra] += seg_sum[rb]
            return ra

        ans = [0] * n
        max_sum = 0

        # Process in reverse: start with everything removed (max_sum = 0)
        for i in range(n - 1, -1, -1):
            ans[i] = max_sum
            idx = removeQueries[i]
            # Activate idx
            active[idx] = True
            parent[idx] = idx
            seg_sum[idx] = nums[idx]
            size[idx] = 1

            # Merge with left neighbor if active
            if idx - 1 >= 0 and active[idx - 1]:
                union(idx, idx - 1)

            # Merge with right neighbor if active
            if idx + 1 < n and active[idx + 1]:
                union(idx, idx + 1)

            # Update global max using root of idx
            root = find(idx)
            if seg_sum[root] > max_sum:
                max_sum = seg_sum[root]

        return ans