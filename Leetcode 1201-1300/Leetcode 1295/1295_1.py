# Leetcode 1295: Find Numbers with Even Number of Digits
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        """
        Finds the count of numbers with an even number of digits in the provided list.
        The function iterates through the list, determines the number of digits
        for each number, and checks if the number of digits is even. If so, it increments
        the count. The final count of such numbers is returned.

        :param nums: A list of integers to analyze.
        :type nums: list[int]
        :return: Number of integers with an even number of digits.
        :rtype: int
        """
        even_digit_count = 0

        # Iterate through each number in the input list
        for num in nums:
            num_digits = len(str(num))

            # Check if the number of digits is even
            if num_digits % 2 == 0:
                even_digit_count += 1

        return even_digit_count