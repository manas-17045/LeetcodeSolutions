# Leetcode 3420: Count Non-Decreasing Subarrays After K Operations
# https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/
# Solved on 26th of July, 2025
from collections import deque


class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        """
        Counts the number of non-decreasing subarrays after at most k operations.

        Args:
            nums: A list of integers representing the array.
            k: An integer representing the maximum allowed operations.
        """

        n = len(nums)
        ans = 0
        cost = 0

        dq = deque()

        j = n - 1

        for i in range((n - 1), -1, -1):
            num_i = nums[i]

            while dq and nums[dq[-1]] < num_i:
                l_idx = dq.pop()

                r_idx = dq[-1] if dq else (j + 1)

                cost += (r_idx - l_idx) * (num_i - nums[l_idx])

            dq.append(i)

            # Shrink the window from the right f the cost is over budget
            while cost > k:
                max_in_window = nums[dq[0]]
                cost -= max_in_window - nums[j]

                # If the rightmost element `j` was the maximum, it must be removed from the deque.
                if dq[0] == j:
                    dq.popleft()

                j -= 1

            # Add the count of valid subarrays.
            ans += j - i + 1

        return ans