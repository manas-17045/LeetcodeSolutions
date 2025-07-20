# Leetcode 2827: Number of Beautiful Integers in the Range
# https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/
# Solved on 20th of July, 2025
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        """
        Calculates the number of beautiful integers in the range [low, high].
        A beautiful integer is defined as a positive integer where the count of even digits
        equals the count of odd digits, and the integer is divisible by k.

        Args:
            low (int): The lower bound of the range (inclusive).
            high (int): The upper bound of the range (inclusive).
            k (int): The divisor for beautiful integers.

        Returns:
            int: The number of beautiful integers in the specified range.
        """
        def count(s: str) -> int:
            memo = {}
            n = len(s)

            def solve(index: int, remainder: int, diff: int, isLeadingZero: bool, isTight: bool) -> int:
                if index == n:
                    return 1 if not isLeadingZero and remainder == 0 and diff == 10 else 0

                state = (index, remainder, diff, isLeadingZero, isTight)
                if state in memo:
                    return memo[state]

                res = 0
                upperBound = int(s[index]) if isTight else 9

                for digit in range(upperBound + 1):
                    newIsTight = isTight and (digit == upperBound)

                    if isLeadingZero and digit == 0:
                        res += solve(index + 1, 0, 10, True, newIsTight)
                    else:
                        newDiff = diff
                        if digit % 2 == 0:
                            newDiff += 1
                        else:
                            newDiff -= 1

                        newRemainder = (remainder * 10 + digit) % k
                        res += solve(index + 1, newRemainder, newDiff, False, newIsTight)

                memo[state] = res
                return res

            return solve(0, 0, 10, True, True)

        highCount = count(str(high))
        lowCount = count(str(low - 1))

        return highCount - lowCount