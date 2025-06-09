# Leetcode 2376: Count Special Integers
# https://leetcode.com/problems/count-special-integers/
# Solved on 9th of June, 2025

class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        """
        Counts the number of positive integers less than or equal to n that have no repeated digits.

        A special integer is a positive integer with no repeated digits.

        Args:
            n: The upper bound (inclusive).
        Returns:
            The count of special integers less than or equal to n.
        """
        numStr = str(n)
        length = len(numStr)
        count = 0

        def permutations(permN, permK):
            if permK < 0 or permK > permN:
                return 0
            res = 1
            for i in range(permK):
                res *= (permN - i)
            return res

        for i in range(1, length):
            count += 9 * permutations(9, i - 1)

        usedDigits = set()
        for i, digitChar in enumerate(numStr):
            digit = int(digitChar)

            startDigit = 1 if i == 0 else 0
            for d in range(startDigit, digit):
                if d not in usedDigits:
                    count += permutations(9 - i, length - 1 - i)

            if digit in usedDigits:
                return count

            usedDigits.add(digit)

        count += 1
        return count