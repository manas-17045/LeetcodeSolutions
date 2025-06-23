# Leetcode 3185: Count Pairs That Form a Complete Day II
# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/
# Solved on 23rd of June, 2025
class Solution:
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        """
        Counts the number of pairs of hours (i, j) such that hours[i] + hours[j] is a multiple of 24.

        Args:
            hours: A list of integers representing the hours.

        Returns:
            The total number of complete day pairs.
        """
        pairCount = 0
        remainderFrequencies = [0] * 24

        for currentHourValue in hours:
            currentRemainer = currentHourValue % 24

            neededRemainder = (24 - currentRemainer) % 24

            pairCount += remainderFrequencies[neededRemainder]

            remainderFrequencies[currentRemainer] += 1

        return pairCount