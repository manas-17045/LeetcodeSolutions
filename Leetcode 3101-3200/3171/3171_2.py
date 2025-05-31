# Leetcode 3171: Find Subarray With Bitwise OR Closest to K
# https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/
# Solved on 31st of May, 2025

class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        # prev_or will store all distinct OR-values of subarrays ending at the previous index.
        prev_or = set()
        ans = float('inf')

        for x in nums:
            # Start a new set for subarrays ending at this index:
            # 1. The single-element subarray [x]
            # 2. Extend each sub-array ending at (r - 1) by OR'ing with x
            curr_or = {x}
            for val in prev_or:
                curr_or.add(val | x)

            # Check each OR-value against k
            for v in curr_or:
                diff = abs(v - k)
                if diff < ans:
                    ans = diff
                    if ans == 0:
                        return 0

            # Move on: this becomes the "previous" set for the next iteration
            prev_or = curr_or

        return ans