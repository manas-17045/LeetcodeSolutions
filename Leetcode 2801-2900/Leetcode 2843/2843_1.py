# Leetcode 2843: Count Symmetric Integers
# https://leetcode.com/problems/count-symmetric-integers/

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        """
        Counts the number of symmetric integers within a specified range. A symmetric
        integer is defined as an integer with an even number of digits where the sum
        of the first half of the digits is equal to the sum of the second half.

        :param low: The start of the range (inclusive) to search for symmetric integers.
        :type low: int
        :param high: The end of the range (inclusive) to search for symmetric integers.
        :type high: int
        :return: The count of symmetric integers within the given range.
        :rtype: int
        """
        symmetric_count = 0

        # Iterate through each number in the given range
        for x in range(low, high + 1):
            # Cpnvert the number to a string to easily access digits
            s = str(x)
            L = len(s)

            # Check if the number of digits is even
            if L % 2 == 0:
                # Calculate the midpoint index
                n = L // 2

                # Calculate the sum of the first half digits
                # Uses slicing s[:n] and a generator expression within sum()
                sum_first_half = sum(int(digit) for digit in s[:n])

                # Calculate the sum of the second half digits
                # Uses slicing s[n:] and a generator expression within sum()
                sum_second_half = sum(int(digit) for digit in s[n:])

                # Check if the sums of the two halves are equal
                if sum_first_half == sum_second_half:
                    symmetric_count += 1

        # Return the total count found
        return symmetric_count