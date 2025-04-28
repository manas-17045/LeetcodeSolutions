# Leetcode 2563: Count the Number of Fair Pairs
# https://leetcode.com/problems/count-the-number-of-fair-pairs/

class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        fair_pair_count = 0

        # --- Optimization using Two Pointers ---
        # We want to count pairs (i, j) such that i < j and
        # lower <= nums[i] + nums[j] <= upper.
        # This is equivalent to:
        # (Count of pairs with nums[i] + nums[j] <= upper)
        # - (Count of pairs with nums[i] + nums[j] <= lower - 1)

        def count_pairs_le(k: int) -> int:
            """
            Counts pairs (i, j) such that i < j and nums[i] + nums[j] <= k.
            Uses a two-pointer approach on the sorted array.
            Time complexity: O(n)
            """
            count = 0
            left, right = 0, n - 1
            while left < right:
                if nums[left] + nums[right] <= k:
                    # If nums[left] + nums[right] <= k, then since the array is sorted,
                    # nums[left] can be paired with any element from index left + 1
                    # up to index right.
                    # The number of such elements (and thus pairs involving nums[left])
                    # is (right - left).
                    count += (right - left)
                    # Move the left pointer to consider the next potential element
                    # for the left side of the pair.
                    left += 1
                else:
                    # If nums[left] + nums[right] > k, the sum is too large.
                    # To potentially decrease the sum, we must move the right pointer inward.
                    right -= 1
            return count

        # Calculate the final count using the inclusion-exclusion principle
        # with the helper function.
        fair_pair_count += count_pairs_le(upper) - count_pairs_le(lower - 1)

        return fair_pair_count
