# Leetcode 1295: Find Numbers with Even Number of Digits
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        even_digit_count = 0

        # Iterate through each number in the input list
        for num in nums:
            num_digits = len(str(num))

            # Check if the number of digits is even
            if num_digits % 2 == 0:
                even_digit_count += 1

        return even_digit_count