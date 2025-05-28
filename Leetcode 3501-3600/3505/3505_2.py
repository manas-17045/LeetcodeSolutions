# Leetcode 3505: Minimum Operations to Make Elements Within K Subarrays Equal
# https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/
# Solved on 27th of May, 2025
import heapq


class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        """
        Given an array nums, an integer x, and an integer k, return the minimum
        number of operations to make elements within k non-overlapping subarrays
        of length x equal. An operation consists of changing an element's value.

        The problem can be broken down into two parts:
        1. For each subarray of length x, calculate the minimum operations to make
           all its elements equal. This is the sum of absolute differences from the
           median. A two-heap approach is used to efficiently calculate this for
           sliding windows.
        2. Use dynamic programming to find the minimum total operations to select
           k non-overlapping subarrays of length x.

        """
        n = len(nums)
        m = n - x + 1
        if m < k:
            return -1

        # Compute cost[i] = min ops to make nums[i:i+x] all equal
        # two‐heap multiset supporting deletions, plus running sums
        low = []    # Max-heap (store negated)
        high = []   # Min-heap
        del_low = {}
        del_high = {}
        sum_low = sum_high = 0
        size_low = size_high = 0

        def prune(heap):
            if heap is low:
                while low and del_low.get(-low[0], 0):
                    val = -heapq.heappop(low)
                    del_low[val] -= 1
            else:
                while high and del_high.get(high[0], 0):
                    val = heapq.heappop(high)
                    del_high[val] = -1

        def rebalance():
            nonlocal sum_low, sum_high, size_low, size_high
            # Low may have at most one more element than high
            if size_low > size_high + 1:
                v = -heapq.heappop(low)
                sum_low -= v
                size_low -= 1
                heapq.heappush(high, v)
                sum_high += v
                size_high += 1
                prune(low)
            elif size_low < size_high:
                v = heapq.heappop(high)
                sum_high -= v
                size_high -= 1
                heapq.heappush(low, -v)
                sum_low += v
                size_low += 1
                prune(high)

        def add(num: int):
            nonlocal sum_low, sum_high, size_low, size_high
            # If low empty or num <= current median, go to low
            if not low or num <= -low[0]:
                heapq.heappush(low, -num)
                sum_low += num
                size_low += 1
            else:
                heapq.heappush(high, num)
                sum_high += num
                size_high += 1
            rebalance()

        def remove(num: int):
            nonlocal sum_low, sum_high, size_low, size_high
            # Guess heap by comparing to median
            median = -low[0]
            if num <= median:
                size_low -= 1
                sum_low -= num
                del_low[num] = del_low.get(num, 0) + 1
                if low and num == -low[0]:
                    prune(low)
            else:
                size_high -= 1
                sum_high -= num
                del_high[num] = del_high.get(num, 0) + 1
                if high and num == high[0]:
                    prune(high)
            rebalance()

        def get_cost() -> int:
            # Sum |a_i - median|
            median = -low[0]
            return median * size_low - sum_low + sum_high - median + size_high

        # Build first window
        for i in range(x):
            add(nums[i])
        cost = [0] * m
        cost[0] = get_cost()
        # Slide
        for i in range(1, m):
            remove(nums[i - 1])
            add(nums[i + x - 1])
            cost[i] = get_cost()

        # DP to pick k non-overlapping windows
        INF = 10**30
        # dp_prev[j] = best cost picking current j windows up to position (i - 1)
        dp_prev = [INF] * m
        # Base j = 1
        dp_prev[0] = cost[0]
        for i in range(1, m):
            dp_prev[i] = min(dp_prev[i - 1], cost[i])

        for j in range(2, k + 1):
            dp_curr = [INF] * m
            for i in range(m):
                if i > 0:
                    dp_curr[i] = dp_curr[i - 1]
                # If we choose window ending at i, prev must end <= (i - x)
                if i >= x and dp_prev[i - x] < INF:
                    dp_curr[i] = min(dp_curr[i], dp_prev[i - x] + cost[i])
            dp_prev = dp_curr

        ans = dp_prev[m - 1]
        return ans if ans < INF else -1