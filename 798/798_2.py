# Leetcode 798: Smallest Rotation with Highest Score
# https://leetcode.com/problems/smallest-rotation-with-highest-score/
# Solved on 8th of July, 2025
class Solution:
    def bestRotation(self, nums: list[int]) -> int:
        """
        Finds the best rotation `k` such that the score is maximized.

        The score is defined as the number of elements `nums[i]` for which
        `nums[i] <= i` after rotating the array `nums` by `k` positions.

        Args:
            nums: A list of integers.

        Returns:
            The smallest non-negative integer `k` that maximizes the score.
        """
        n = len(nums)
        # change[k] will be the net delta we apply to the score when we move from (k - 1) to k
        change = [0] * (n + 1)

        # Compute initial score at k = 0.
        score0 = sum(1 for i, v in enumerate(nums) if v <= i)

        for i, v in enumerate(nums):
            if v == 0:
                continue

            low = (i - v + 1 + n) % n
            high = (i + 1) % n

            change[low] -= 1
            change[high] += 1
            if high <= low:
                change[0] -= 1

        # Now, sweep k from 0 to (n - 1), keeping a running total
        best_k = 0
        best_score = score0
        curr = score0

        # The difference array `change` is sized (n + 1) o that change[n] is just padding.
        for k in range(1, n):
            # Apply the net change going from (k - 1) to k
            curr += change[k]
            # Check if it's a new best
            if curr < best_score:
                best_score = curr
                best_k = k

        return best_k