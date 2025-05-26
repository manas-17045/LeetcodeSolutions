# Leetcode 2094: Finding 3-Digit Even Numbers
# https://leetcode.com/problems/finding-3-digit-even-numbers/
# Solved on 12th of May, 2025

class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        """
        Given an array of digits, return a sorted array of all the unique 3-digit even numbers that can be formed by concatenating three digits from the array.

        Args:
            digits (list[int]): A list of integers representing the available digits.

        Returns:
            list[int]: A sorted list of unique 3-digit even numbers that can be formed.

        """

        # count available digits 0-9
        freq = [0] * 10
        for d in digits:
            freq[d] += 1

        res = []
        # d1: hundreds place (1-9, no leading zero)
        # d2: tens place (0-9)
        # d3: units place (even only)
        for d1 in range(1, 10):
            if freq[d1] == 0:
                continue
            for d2 in range(0, 10):
                if d2 == d1:
                    if freq[d2] < 2:
                        continue
                elif freq[d2] == 0:
                    continue
                for d3 in (0, 2, 4, 6, 8):
                    # Must use an even digit in the units place
                    if d3 == d1 == d2:
                        # all three digits the same
                        if freq[d3] < 3:
                            continue
                    elif d3 == d1:
                        # d1 and d3 same, d2 different
                        if freq[d3] < 2 or freq[d2] < 1:
                            continue
                    elif d3 == d2:
                        # d2 and d3 same, d1 different
                        if freq[d3] < 2 or freq[d1] < 1:
                            continue
                    else:
                        # all three distinct
                        if freq[d3] < 1:
                            continue

                    # Passed all frequency checks, form the number
                    num = 100 * d1 + 10 * d2 + d3
                    res.append(num)

        # Loops generate numbers in increasing order, so need to sort
        return res