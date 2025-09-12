# Leetcode 2564: Substring XOR Queries
# https://leetcode.com/problems/substring-xor-queries/
# Solved on 12th of September, 2025
class Solution:
    def substringXorQueries(self, s: str, queries: list[list[int]]) -> list[list[int]]:
        """
        Finds the starting and ending indices of substrings in 's' that, when interpreted as binary numbers,
        satisfy an XOR query.

        Args:
            s (str): A binary string.
            queries (list[list[int]]): A list of queries, where each query is [first, second].

        Returns:
            list[list[int]]: A list of results, where each result is [start_index, end_index] for a matching substring, or [-1, -1] if no such substring is found.
        """

        n = len(s)
        valMap = {}

        for length in range(1, 33):
            if length > n:
                break

            currentVal = int(s[0:length], 2)
            if currentVal not in valMap:
                valMap[currentVal] = [0, (length - 1)]

            mask = (1 << length) - 1

            for i in range(1, (n - length + 1)):
                currentVal = ((currentVal << 1) & mask) | int(s[i + length - 1])

                if currentVal not in valMap:
                    valMap[currentVal] = [i, (i + length - 1)]

        result = []
        for first, second in queries:
            targetVal = first ^ second
            result.append(valMap.get(targetVal, [-1, -1]))

        return result