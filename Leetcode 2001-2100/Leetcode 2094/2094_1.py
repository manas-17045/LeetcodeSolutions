# Leetcode 2094: Finding 3-Digit Even Numbers
# https://leetcode.com/problems/finding-3-digit-even-numbers/
# Solved on 12th May, 2025
from collections import Counter


class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        """
        Given an integer array digits, return a sorted array of all the unique integers that can be formed by concatenating three elements in digits such that the integer is even.

        For example, if digits = [1, 2, 3], the possible integers are [132, 312].

        Args:
            digits (list[int]): A list of integers representing the digits available to form numbers.

        Returns:
            list[int]: A sorted list of unique 3-digit even numbers that can be formed using the digits.
        """

        input_counts = Counter(digits)
        result = []

        # Iterate through all possible 3-digit even numbers.
        # Smallest 3-digit even number is 100.
        # Largest 3-digit even number is 998.
        # The loop range(100, 100, 2) covers 100, 102, ..., 998.
        # This automatically handles:
        # 1. The number is 3-digits.
        # 2. The number does not have leading zeros (since we start at 100).
        # 3. The number is even (due to the step of 2).
        for num in range(100, 1000, 2):
            # Extract digits for the current number `num`.
            # For num = abc, d1 = a, d2 = b, d3 = c
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10

            # Create a frequency map for the digits required to form `num`
            required_digits_counts = Counter([d1, d2, d3])

            # Check if 'num' can be formed using the available digits from 'input_counts'
            can_form_num = True
            for digit_val, count_needed in required_digits_counts.items():
                # collections.Counter defaults to 0 for missing keys,
                # So, if a digit_val is needed but not in input_counts,
                # input_counts[digit_val] will be 0.
                if input_counts[digit_val] < count_needed:
                    can_form_num = False
                    break   # Not enough of this digit_val available

            if can_form_num:
                result.append(num)

        # The 'result' list is already sorted because 'num' is iterated in increasing order.
        # Each 'num' from the range is unique, so 'result' will contain unique integers
        # if they are formidable.
        return result