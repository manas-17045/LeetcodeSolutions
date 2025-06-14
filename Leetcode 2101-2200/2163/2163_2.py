# Leetcode 2163: Minimum Difference in Sums After Removal of Elements
# https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/
# Solved on 14th of June, 2025
import heapq


class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        """
        Given an integer array nums of size 3 * n, you have to find a subsequence of size n
        such that the difference between the sum of the first n elements of the subsequence
        and the sum of the last n elements is minimum.

        The problem can be rephrased as partitioning the 3*n elements into three groups of size n.
        We want to minimize the difference between the sum of the first group and the sum of the third group.
        The middle group's elements are essentially discarded.

        We can iterate through all possible split points between the first and third groups.
        For a split point `i` (where the first group ends at index `i-1` and the third group starts at index `i`),
        the first group must consist of `n` elements from `nums[0:i]` and the third group must consist of `n`
        elements from `nums[i:3*n]`.

        To minimize the difference (sum of first n - sum of last n), we need to maximize the sum of the last n
        elements and minimize the sum of the first n elements for a given split point.

        This can be efficiently computed using two passes and heaps.
        """
        total = len(nums)
        N = total // 3

        # Compute left_sum[i]: min sum of N elements from nums[0:i]
        left_sum = [0] * (total + 1)
        max_heap = []
        curr = 0
        # init with first N elements
        for x in nums[:N]:
            curr += x
            heapq.heappush(max_heap, -x)
        left_sum[N] = curr

        # Extend i from N to 2N - 1, inserting nums[i]
        for i in range(N, 2 * N):
            x = nums[i]
            curr += x
            heapq.heappush(max_heap, -x)
            # Pop the largest among the heap to keep size == N
            mx = -heapq.heappop(max_heap)
            curr -= mx
            left_sum[i + 1] = curr

        # Compute right_sum[i]: max sum of N elements from nums[i:total]
        right_sum = [0] * (total + 1)
        min_heap = []
        curr = 0
        # init with last N elements
        for x in nums[2 * N:]:
            curr += x
            heapq.heappush(min_heap, x)
        right_sum[2 * N] = curr

        # Extend backwards from 2N - 1 down to N
        for i in range(2 * (N - 1), (N - 1), -1):
            x = nums[i]
            curr += x
            heapq.heappush(min_heap, x)
            # Pop the smallest to keep size == N
            mn = heapq.heappop(min_heap)
            curr -= mn
            right_sum[i] = curr

        # Take the minimum difference
        ans = float('inf')
        for i in range(N, 2 * N + 1):
            ans = min(ans, left_sum[i] - right_sum[i])

        return ans