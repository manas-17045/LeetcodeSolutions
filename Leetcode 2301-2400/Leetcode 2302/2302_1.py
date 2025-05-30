# Leetcode 2302: Count Subarrays With Score Less Than K
# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        """
        Counts the number of non-empty subarrays whose score is strictly less than k.
        The score of a subarray is defined as (sum of elements) * (length of subarray).

        Args:
            nums: A list of positive integers. Constraints: nums.length >= 1, nums[i] >= 1.
            k: An integer threshold. Constraint: k >= 1.

        Returns:
            The total number of subarrays with score < k.

        Algorithm:
        This solution uses the sliding window (two pointers) technique, which is
        efficient for problems involving contiguous subarrays and monotonic properties.
        1. Initialize count, left pointer `l`, and `current_sum` to 0.
        2. Iterate through the array with a right pointer `r`.
        3. Expand the window by adding `nums[r]` to `current_sum`.
        4. Calculate the score of the current window `nums[l...r]`:
           `score = current_sum * (r - l + 1)`.
        5. While the score is too high (`>= k`), and the window is valid (`l <= r`):
           - Shrink the window from the left by subtracting `nums[l]` from `current_sum`.
           - Increment the left pointer `l`.
           - Recalculate the score for the shrunken window.
        6. After shrinking (or if shrinking wasn't needed), the window `nums[l..r]`
           satisfies `score < k`. Due to the monotonicity (positive numbers), all
           subarrays ending at `r` and starting at any index `i` where `l <= i <= r`
           will also have a score less than `k`.
        7. The number of such valid subarrays ending at `r` is `r - l + 1`. Add this
           to the total `count`.
        8. Continue until `r` reaches the end of the array.
        9. Return the total `count`.
        """
        count = 0
        current_sum = 0
        l = 0 # Left pointer of the sliding window
        n = len(nums)

        for r in range(n):
            # Expand the window by including the element at index r
            current_sum += nums[r]

            # Calculate the score of the current window [l...r]
            current_length = r - l + 1
            current_score = current_sum * current_length

            # While the score is too high, shrink the window from the left
            # Ensure l <= r to keep the window valid during shrinking
            while current_score >= k and l <= r:
                # Remove the element at index l from the sum
                current_sum -= nums[l]
                # Move the left pointer one step to the right
                l += 1

                # Recalculate the length and score for the new window [l...r]
                current_length = r - l + 1
                # If the window becomes empty (l > r), length is 0, sum is 0, score is 0
                if current_length <= 0:
                    current_score = 0
                else:
                    current_score = current_sum * current_length

            # The loop condition `current_score >= k` will handle exiting if score becomes < k.
            # At this point, the window [l...r] has a score < k.
            # All subarrays ending at r and starting at or after l are valid.
            # The number of subarrays id r - l + 1.
            # If l > r (window became empty), r - l - 1 is <= 0, adding 0 correctly.
            count += (r - l + 1)

        return count