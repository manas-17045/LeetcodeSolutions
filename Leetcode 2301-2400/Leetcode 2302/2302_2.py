# Leetcode 2302: Count Subarrays With Score Less Than K
# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        count = 0
        current_sum = 0
        left = 0

        for right in range(n):
            # Add the current element to our running sum
            current_sum += nums[right]

            # While the current window's score is >= k, shrink the window from the left
            while left <= right and current_sum * (right - left + 1) >= k:
                current_sum -= nums[left]
                left += 1

            # All subarrays ending at the right position with left boundary from left to right have score < k.
            count += right - left + 1

        return count