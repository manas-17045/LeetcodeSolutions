# Leetcode 3420: Count Non-Decreasing Subarrays After K Operations
# https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/
# Solved on 26th of July, 2025
from collections import deque


class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        """
        Counts the number of non-decreasing subarrays where the cost of making them non-decreasing is at most k.
        :param nums: A list of integers.
        :param k: The maximum allowed cost.
        :return: The total count of such subarrays.
        """

        n = len(nums)
        ans = 0
        cost = 0

        j = n - 1

        dq = deque()

        for i in range((n - 1), -1, -1):
            v = nums[i]
            cnt = 1

            while dq and dq[-1][0] < v:
                val, c = dq.pop()
                cnt += c
                cost += (v - val) * c

            dq.append((v, cnt))

            # Now, shrink from the left while over budget
            while cost > k:
                val, c = dq[0]
                # Remove exactly one element from this block
                dq.popleft()

                cost -= (val - nums[j])
                j -= 1

                # If the block had more than 1, put back the rest
                if c > 1:
                    dq.appendleft((val, c - 1))

            ans += j - i + 1

        return ans