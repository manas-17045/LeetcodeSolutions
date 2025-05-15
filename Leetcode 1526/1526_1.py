# Leetcode 1526: Minimum Number of Increments on Subarrays to Form a Target Array
# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/
# Solved on 15th of May, 2025

class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        """
        Calculates the minimum number of increment operations needed to transform an array of zeros
        into a given target array.  Each operation can increment a subarray by 1.

        Args:
            target: A list of integers representing the target array.

        Returns:
            The minimum number of increment operations required.
        """
        num_operations = 0
        # This variable holds the value of the target element at the previous position.
        # For the first element, we consider the "ground" or initial state to be 0.
        previous_element_value = 0

        for current_element_value in target:
            # If the current target element's value is greater than the previous one,
            # it means we need to perform additional operations.
            # These operations account for the "rise" in the target profile.
            # The number of new operations needed is the difference between
            # the current element's value and the previous one.
            if current_element_value > previous_element_value:
                num_operations += (current_element_value - previous_element_value)

            # Update the previous_element_value for the next iteration.
            previous_element_value = current_element_value

        return num_operations