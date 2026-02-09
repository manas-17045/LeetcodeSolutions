# Leetcode 3835: Count Subarrays With Cost Less Than or Equal to K
# https://leetcode.com/problems/count-subarrays-with-cost-less-than-or-equal-to-k/
# Solved on 9th of February, 2026
from collections import deque


class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        """
        Counts the number of subarrays where the cost is less than or equal to k.
        The cost is defined as (max(subarray) - min(subarray)) * length(subarray).

        :param nums: List of integers representing the input array.
        :param k: The maximum allowable cost for a subarray.
        :return: Total count of subarrays satisfying the condition.
        """
        count = 0
        left = 0
        maxDeque = deque()
        minDeque = deque()
        n = len(nums)

        for right in range(n):
            while maxDeque and nums[maxDeque[-1]] <= nums[right]:
                maxDeque.pop()
            maxDeque.append(right)

            while minDeque and nums[minDeque[-1]] >= nums[right]:
                minDeque.pop()
            minDeque.append(right)

            while (nums[maxDeque[0]] - nums[minDeque[0]]) * (right - left + 1) > k:
                left += 1
                if maxDeque[0] < left:
                    maxDeque.popleft()
                if minDeque[0] < left:
                    minDeque.popleft()

            count += (right - left + 1)

        return count