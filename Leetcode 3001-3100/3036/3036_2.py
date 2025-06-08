# Leetcode 3036: Number of Subarrays That match a Pattern II
# https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/
# Solved on 8th of June, 2025

class Solution:
    def countMatchingSubarrays(self, nums: list[int], pattern: list[int]) -> int:
        """
        Counts the number of subarrays in `nums` that match the given `pattern`.

        A subarray `nums[i...i+m]` matches the pattern if for all `k` from 0 to `m-1`:
        - `nums[i+k+1] > nums[i+k]` if `pattern[k] == 1`
        - `nums[i+k+1] == nums[i+k]` if `pattern[k] == 0`
        - `nums[i+k+1] < nums[i+k]` if `pattern[k] == -1`

        This solution uses the Knuth-Morris-Pratt (KMP) algorithm to efficiently find
        occurrences of the pattern in the sequence of pairwise comparisons of `nums`.

        Args:
            nums: A list of integers.
            pattern: A list of integers representing the pattern (1, 0, or -1).

        Returns:
            The number of matching subarrays.
        """
        n, m = len(nums), len(pattern)
        # Need at least (m + 1) elements to form a window
        if n < m + 1:
            return 0

        # Build KMP "failure" function on pattern
        pi = [0] * m
        j = 0
        for i in range(1, m):
            while j and pattern[i] != pattern[j]:
                j = pi[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            pi[i] = j

        # Now, scan nums pairwise, feeding comparisons into the KMP matcher
        ans = 0
        j = 0
        for i in range(n - 1):
            # Compute the comparison result between nums[i] and nums[i + 1]
            if nums[i + 1] > nums[i]:
                x = 1
            elif nums[i + 1] == nums[i]:
                x = 0
            else:
                x = -1

            # KMP step
            while j and x != pattern[j]:
                j = pi[j - 1]
            if x == pattern[j]:
                j += 1

            # Full Match => one matching window ends at (i + 1)
            if j == m:
                ans += 1
                j = pi[j - 1]

        return ans