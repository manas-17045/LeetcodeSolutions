# Leetcode 2100: Find Good Days to Rob the Bank
# https://leetcode.com/problems/find-good-days-to-rob-the-bank/
# Solved on 10th of August, 2025
class Solution:
    def goodDaysToRobBank(self, security: list[int], time: int) -> list[int]:
        """
        Finds all days when a bank can be robbed. A bank can be robbed on day `i` if:
        - The security values for `time` days before day `i` are non-increasing.
        - The security values for `time` days after day `i` are non-decreasing.
        :param security: A list of integers representing the security values on different days.
        :param time: An integer representing the number of days before and after the current day to check.
        :return: A list of integers representing the indices of the days when the bank can be robbed.
        """
        n = len(security)
        if time == 0:
            return list(range(n))

        if n < 2 * time + 1:
            # Not enough days to have `time` days before and after
            return []

        non_inc = [0] * n
        for i in range(1, n):
            if security[i - 1] >= security[i]:
                non_inc[i] = non_inc[i - 1] + 1
            else:
                non_inc[i] = 0

        non_dec = [0] * n
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                non_dec[i] = non_dec[i + 1] + 1
            else:
                non_dec[i] = 0

        res = []
        for i in range(n):
            if non_inc[i] >= time and non_dec[i] >= time:
                res.append(i)

        return res