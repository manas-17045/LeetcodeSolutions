# Leetcode 3528: Unit Conversion I
# https://leetcode.com/problems/unit-conversion-i/
# Solved on 30th of December, 2025
class Solution:
    def baseUnitConversions(self, conversions: list[list[int]]) -> list[int]:
        """
        Calculates the conversion factors from unit 0 to all other units.
        :param conversions: A list of conversion rules, where each rule is [source, target, factor].
        :return: A list where result[i] is the conversion factor from unit 0 to unit i.
        """
        n = len(conversions) + 1
        graph = [[] for _ in range(n)]
        for source, target, factor in conversions:
            graph[source].append((target, factor))

        result = [0] * n
        result[0] = 1
        modulo = 10 ** 9 + 7
        stack = [0]

        while stack:
            current = stack.pop()
            currentValue = result[current]

            for neighbor, factor in graph[current]:
                result[neighbor] = (currentValue * factor) % modulo
                stack.append(neighbor)

        return result