# Leetcode 2348: Number of Zero-Filled Subarrays
# https://leetcode.com/problems/number-of-zero-filled-subarrays/
# Solved on 20th of May, 2025

class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        """
        Counts the number of subarrays filled with zeros in a given list of integers. It iterates through the list,
        tracking consecutive zeros and calculating the number of subarrays formed by each run of zeros.
        """
        total_zero_subarrays = 0
        current_streak_of_zeros = 0

        # Iterate through each number in the input array
        for num in nums:
            if num == 0:
                # If the number is 0, extend the current streak of zeros
                current_streak_of_zeros += 1
            else:
                # If the number is non-zero, the streak of zeros (if any) has ended.
                # Add the count of zero-filled subarrays from this streak to the total.
                # A streak of length k contributes k * (k + 1) / 2 subarrays.
                if current_streak_of_zeros > 0:
                    count_from_streak = current_streak_of_zeros * (current_streak_of_zeros + 1) // 2
                    total_zero_subarrays += count_from_streak

                # Reset the streak counter as the current number is non-zero
                current_streak_of_zeros = 0

        # After the loop, there might be a pending streak if the array ends with zeros.
        # Add the count of zero-filled subarrays from this final streak.
        if current_streak_of_zeros > 0:
            count_from_final_streak = current_streak_of_zeros * (current_streak_of_zeros + 1) // 2
            total_zero_subarrays += count_from_final_streak

        return total_zero_subarrays