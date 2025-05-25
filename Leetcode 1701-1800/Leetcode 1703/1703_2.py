# Leetcode 1703: Minimum Adjacent Swaps for K Consecutive Ones
# https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/
# Solved on 17th of May, 2025

class Solution:
    def minMoves(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum number of adjacent swaps required to group k consecutive 1s in a binary array.

        Args:
            nums: A list of integers representing the binary array.
            k: The number of consecutive 1s to group.

        Returns:
            The minimum number of adjacent swaps needed.  Returns 0 if no solution is possible (e.g., k > number of 1s).

        Algorithm:  Transforms the problem into minimizing the sum of distances of 1s to a median position within
                    a sliding windows of size k.  Uses prefix sums for efficiency.
        """
        # Collect indices of all the 1's
        pos = [i for i, v in enumerate(nums) if v == 1]

        # Build the "shifted" array b[i] = pos[i] - i
        b = [p - i for i, p in enumerate(pos)]

        # Prefix sums of b for fast range-sum queries
        n = len(b)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + b[i]

        ans = float('inf')
        # Slide over every window of size k in b
        for i in range(0, n - k + 1):
            j = i + k - 1
            mid = (i + j) // 2
            median = b[mid]

            # Cost to bring left half up to median
            left_cnt = mid - i
            left_sum = pre[mid] - pre[i]
            left_cost = median * left_cnt - left_sum

            # Cost to bring right half down to median
            right_cnt = j - mid
            right_sum = pre[j + 1] - pre[mid + 1]
            right_cost = right_sum - median * right_cnt

            # Total adjacent-swap moves for this block
            total = left_cost + right_cost
            ans = min(ans, total)

        return ans if ans != float('inf') else 0