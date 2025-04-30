# Leetcode 1295: Find Numbers with Even Number of Digits
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
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