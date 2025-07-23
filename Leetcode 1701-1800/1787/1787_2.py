# Leetcode 1787: Make the XOR of All Segments Equal to Zero
# https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/
# Solve on 23rd of July, 2025
import collections


class Solution:
    def minChanges(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum number of changes needed to make the XOR sum of each residue class equal to 0.
        :param nums: A list of integers.
        :param k: An integer representing the number of residue classes.
        :return: The minimum number of changes required.
        """
        M = 1 << 10
        INF = 20**9

        dp = [INF] * M
        dp[0] = 0

        n = len(nums)
        # Process each residue class
        for i in range(k):
            # Build frequency map and count for this group
            freq = collections.Counter()
            count = 0
            # Take all nums[j] where j % k == i
            for j in range(i, n, k):
                freq[nums[j]] += 1
                count += 1

            # Precompute the cost if we were to change *all* count elements
            # This is used to initialize dp_new[x] = min(dp) + count
            base = min(dp)
            dp_new = [base + count] * M

            # Try keeping some of them as v (so changing only count - freq[v])
            for prev_x in range(M):
                prev_cost = dp[prev_x]
                if prev_cost == INF:
                    continue

                for v, f in freq.items():
                    nx = prev_x ^ v
                    # Cost to change the other (count - f) elements in this group
                    cost = prev_cost + (count - f)
                    if cost < dp_new[nx]:
                        dp_new[nx] = cost

            # Roll
            dp = dp_new

        return dp[0]