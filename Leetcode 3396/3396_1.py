# Leetcode 3396: Minimum Number of Operations to Make Elements in Array Distinct
# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        Calculate the minimum number of operations required to ensure that every suffix
        of the input list becomes distinct. An operation consists of advancing the start
        index by 3 and repeating the check for distinct elements in the remaining suffix.

        The function iteratively checks if a suffix of the input list (starting from a
        given index) contains only distinct elements. If a duplicate is found, an operation
        is performed to adjust the suffix to be checked. The process continues until a
        suffix with only distinct elements is encountered.

        :param nums: A list of integers to examine and transform so that every suffix
            starting from a given index contains distinct values
        :return: The minimum number of operations required to ensure all suffixes
            are distinct
        :rtype: int
        """
        n = len(nums)
        operations = 0
        start_index = 0

        # Continue as long as there are elements to potentially check
        while start_index < n:
            # Check if the current suffix nums[start_index:] has distinct elements
            seen = set()
            is_distinct = True

            # Iterate through the elements of the current suffix
            for i in range(start_index, n):
                if nums[i] in seen:
                    # Found a duplicate, this suffix is not distinct
                    is_distinct = False
                    break   # No need t check further in this suffix
                # Add the unique element to the set
                seen.add(nums[i])

            # If the suffix was distinct, we've found our answer
            if is_distinct:
                return operations

            # If the suffix was not distinct, perform one operation:
            # Increment the operation count
            operations += 1

            # Advance the start index for the next suffix check
            start_index += 3

        # If the loop completes, it means start_index >= n.
        # This implies the remaining array is empty, which is considered distinct.
        # The final value of 'operations' is the answer.
        return operations