# Leetcode 2779: Maximum Beauty of an Array After Applying Operation
# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/
# Solved on 19th of June, 2025

class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        """
        Given a 0-indexed integer array nums and a non-negative integer k, a number x is beautiful if there exists at least one index i in the array such that nums[i] is in the range [x - k, x + k].

        The beauty of an array is the number of beautiful integers in the range [0, 10^5].

        Return the maximum possible beauty of the array nums.

        This solution uses a sweep line approach to find the maximum overlap of intervals [num - k, num + k].
        """
        # Build "enter" and "exit" events for each interval [(num - k), (num + k)]
        events = []
        for num in nums:
            events.append(((num - k), 1))
            events.append(((num + k + 1), -1))

        # Sweep through sorted events, accumulating overlap counts
        events.sort()
        curr = 0
        best = 0
        for _, delta in events:
            curr += delta
            if curr > best:
                best = curr

        return best