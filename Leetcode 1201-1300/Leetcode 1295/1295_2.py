# Leetcode 1295: Find Numbers with Even Number of Digits
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        """
        Finds the count of numbers with an even number of digits in the provided list.

        This function iterates through a list of integers and determines how many of
        them have an even number of digits. It calculates the digit count of each number
        and checks if it is divisible by 2 to confirm it is even. The function returns
        the total count of such numbers.

        :param nums: A list of integers.
        :type nums: list[int]
        :return: The count of numbers with an even number of digits.
        :rtype: int
        """
        count = 0

        for num in nums:
            # Count the number of digits in the current number
            digits = 0

            # Iteratively count digits
            temp = num
            while temp > 0:
                temp //= 10
                digits += 1

            # Check if the number of digits is even
            if digits % 2 == 0:
                count += 1

        return count