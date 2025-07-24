# Leetcode 1363: Largest Multiple of Three
# https://leetcode.com/problems/largest-multiple-of-three/
# Solved on 24th of July, 2025
import collections


class Solution:
    def largestMultipleOfThree(self, digits: list[int]) -> str:
        """
        Given a list of digits, return the largest multiple of three that can be formed
        by concatenating some of the given digits in any order.
        If no such multiple of three can be formed, return an empty string.

        Args:
            digits: A list of integers representing the available digits.
        Returns:
            A string representing the largest multiple of three, or "0" if the only possible multiple is 0, or "" if no multiple can be formed.
        """

        totalSum = sum(digits)
        digitCounts = collections.Counter(digits)

        remOneDigits = [1, 4, 7]
        remTwoDigits = [2, 5, 8]

        remainder = totalSum % 3

        if remainder == 1:
            removedOne = False
            for d in remOneDigits:
                if digitCounts[d] > 0:
                    digitCounts[d] -= 1
                    removedOne = True
                    break

            if not removedOne:
                toRemove = 2
                for d in remTwoDigits:
                    take = min(digitCounts[d], toRemove)
                    digitCounts[d] -= take
                    toRemove -= take
                    if toRemove == 0:
                        break

        elif remainder == 2:
            removedOne = False
            for d in remTwoDigits:
                if digitCounts[d] > 0:
                    digitCounts[d] -= 1
                    removedOne = True
                    break

            if not removedOne:
                toRemove = 2
                for d in remOneDigits:
                    take = min(digitCounts[d], toRemove)
                    digitCounts[d] -= take
                    toRemove -= take
                    if toRemove == 0:
                        break

        elif remainder == 2:
            removedOne = False
            for d in remTwoDigits:
                if digitCounts[d] > 0:
                    digitCounts[d] -= 1
                    removedOne = True
                    break

            if not removedOne:
                toRemove = 2
                for d in remOneDigits:
                    take = min(digitCounts[d], toRemove)
                    digitCounts[d] -= take
                    toRemove -= take
                    if toRemove == 0:
                        break

        resultBuilder = []
        for d in range(9, -1, -1):
            if digitCounts[d] > 0:
                resultBuilder.append(str(d) * digitCounts[d])

        finalString = "".join(resultBuilder)

        if len(finalString) > 0 and finalString[0] == '0':
            return "0"

        return finalString