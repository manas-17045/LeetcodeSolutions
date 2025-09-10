# Leetcode 2151: Maximum Good People Based on Statements
# https://leetcode.com/problems/maximum-good-people-based-on-statements/
# Solved on 10th of September, 2025
class Solution:
    def maximumGood(self, statements: list[list[int]]) -> int:
        """
        Determines the maximum number of good people possible given a set of statements.

        Args:
            statements (list[list[int]]): A 2D list where statements[i][j] represents
                                           the statement made by person i about person j.
                                           0 means person i says person j is bad.
                                           1 means person i says person j is good.
                                           2 means person i made no statement about person j.

        Returns:
            int: The maximum number of good people that can exist in a consistent scenario.
        """
        numPeople = len(statements)
        maxGood = 0

        for currentMask in range((1 << numPeople) - 1, -1, -1):
            countGood = bin(currentMask).count('1')

            if countGood <= maxGood:
                continue

            isPossible = True
            for personI in range(numPeople):
                isPersonIGood = (currentMask >> personI) & 1

                if isPersonIGood:
                    for personJ in range(numPeople):
                        statement = statements[personI][personJ]

                        if statement == 2:
                            continue

                        isPersonJGood = (currentMask >> personJ) & 1

                        if statement != isPersonJGood:
                            isPossible = False
                            break

                if not isPossible:
                    break

            if isPossible:
                maxGood = countGood

        return maxGood