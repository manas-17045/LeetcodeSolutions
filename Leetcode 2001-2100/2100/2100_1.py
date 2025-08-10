# Leetcode 2100: Find Good Days to Rob the Bank
# https://leetcode.com/problems/find-good-days-to-rob-the-bank/
# Solved on 10th of August, 2025
class Solution:
    def goodDaysToRobBank(self, security: list[int], time: int) -> list[int]:
        """
        Finds all good days to rob the bank. A day `i` is a good day if:
        - For all days `j` in `[i - time, i]`, `security[j] >= security[j + 1]` (non-increasing).
        - For all days `j` in `[i, i + time]`, `security[j] <= security[j + 1]` (non-decreasing).
        :param security: A list of integers representing the security values on different days.
        :param time: An integer representing the required non-increasing/non-decreasing period.
        :return: A list of integers representing the indices of good days to rob the bank.
        """
        numDays = len(security)

        if time == 0:
            return list(range(numDays))

        nonIncreasing = [0] * numDays
        for i in range(1, numDays):
            if security[i - 1] >= security[i]:
                nonIncreasing[i] = nonIncreasing[i - 1] + 1

        nonDecreasing = [0] * numDays
        for i in range(numDays - 2, -1, -1):
            if security[i] <= security[i + 1]:
                nonDecreasing[i] = nonDecreasing[i + 1] + 1

        goodDays = []
        for i in range(time, numDays - time):
            hasNonIncreasingBefore = nonIncreasing[i] >= time
            hasNonDecreasingAfter = nonDecreasing[i] >= time
            if hasNonIncreasingBefore and hasNonDecreasingAfter:
                goodDays.append(i)

        return goodDays