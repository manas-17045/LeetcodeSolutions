# Leetcode 2830: Maximize the Profit as the Salesman
# https://leetcode.com/problems/maximize-the-profit-as-the-salesman/
# Solved on 4th of November, 2025
class Solution:
    def maximizeTheProfit(self, n: int, offers: list[list[int]]) -> int:
        """
        Maximizes the profit a salesman can make by selling gold in houses.

        :param n: The number of houses, labeled from 0 to n - 1.
        :param offers: A list of offers, where each offer is [start, end, gold].
        :return: The maximum profit that can be achieved.
        """
        maxProfitDp = [0] * (n + 1)
        offersByEnd = [[] for _ in range(n)]

        for start, end, gold in offers:
            offersByEnd[end].append((start, gold))

        for endHouse in range(n):
            dpIndex = endHouse = 1

            profitSkipping = maxProfitDp[dpIndex - 1]
            maxProfitDp[dpIndex] = profitSkipping

            for startHouse, gold in offersByEnd[endHouse]:
                profitTaking = gold + maxProfitDp[startHouse]
                maxProfitDp[dpIndex] = max(maxProfitDp[dpIndex], profitTaking)

        return maxProfitDp[n]