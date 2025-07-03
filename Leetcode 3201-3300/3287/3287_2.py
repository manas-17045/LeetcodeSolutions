# Leetcode 3287: Find the Maximum Sequence Value of Array
# https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/
# Solved on 3rd of July, 2025
class Solution:
    def maxValue(self, nums: list[int], k: int) -> int:
        """
        This problem asks us to find the maximum possible XOR sum of two subsequences,
        each of length k, chosen from the input array `nums`.
        The two subsequences must be disjoint.

        The approach uses dynamic programming to precompute all possible XOR sums
        for subsequences of length `c` ending at a certain index (for `left_dp`)
        or starting at a certain index (for `right_dp`).

        `left_dp[c]` stores all possible XOR sums of subsequences of length `c`
        from `nums[0...i]`.
        `right_dp[s][c]` stores all possible XOR sums of subsequences of length `c`
        from `nums[s...n-1]` (using reversed array `rev`).
        """
        n = len(nums)
        rev = nums[::-1]

        right_dp = [[set() for _ in range(k + 1)] for __ in range(n + 1)]
        right_dp[0][0].add(0)
        for s in range(1, (n + 1)):
            x = rev[s - 1]
            right_dp[s][0].add(0)
            for c in range(1, (min(s, k) + 1)):
                prev_same = right_dp[s - 1][c]
                prev_less = right_dp[s - 1][c - 1]
                right_dp[s][c].update(prev_same)
                for v in prev_less:
                    right_dp[s][c].add(v | x)


        ans = 0
        left_dp = [set() for _ in range(k + 1)]
        left_dp[0].add(0)
        for i, x in enumerate(nums, start=1):
            for c in range(min(i, k), 0, -1):
                for v in list(left_dp[c - 1]):
                    left_dp[c].add(v | x)

            if i >= k and (n - i) >= k:
                left_set = left_dp[k]
                right_set = right_dp[n - i][k]

                local_max = 0
                for a in left_set:
                    for b in right_set:
                        vb = a ^ b
                        if vb > local_max:
                            local_max = vb
                if local_max > ans:
                    ans = local_max

        return ans