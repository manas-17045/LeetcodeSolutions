# Leetcode 2055: Plates Between Candles
# https://leetcode.com/problems/plates-between-candles/
# Solved on 7th of November, 2025
class Solution:
    def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
        """
        Calculates the number of plates between candles for given queries.

        Args:
            s (str): A string representing plates '*' and candles '|'.
            queries (list[list[int]]): A list of query ranges [left, right].
        Returns:
            list[int]: A list of integers, where each element is the number of plates
                       between candles for the corresponding query.
        """

        n = len(s)

        prefixPlates = [0] * (n + 1)
        for i in range(n):
            prefixPlates[i + 1] = prefixPlates[i]
            if s[i] == '*':
                prefixPlates[i + 1] += 1

        prevCandle = [-1] * n
        lastSeenCandle = -1
        for i in range(n):
            if s[i] == '|':
                lastSeenCandle = i
            prevCandle[i] = lastSeenCandle

        nextCandle = [-1] * n
        lastSeenCandle = -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                lastSeenCandle = i
            nextCandle[i] = lastSeenCandle

        results = []
        for query in queries:
            qLeft = query[0]
            qRight = query[1]

            firstCandle = nextCandle[qLeft]
            lastCandle = prevCandle[qRight]

            if firstCandle == -1 or lastCandle == -1 or firstCandle >= lastCandle:
                results.append(0)
            else:
                plateCount = prefixPlates[lastCandle + 1] - prefixPlates[firstCandle]
                results.append(plateCount)

        return results