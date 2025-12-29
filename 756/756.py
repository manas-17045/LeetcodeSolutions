# Leetcode 756: Pyramid Transition Matrix
# https://leetcode.com/problems/pyramid-transition-matrix/
# Solved on 29th of December, 2025
from collections import defaultdict


class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        """
        Determines if a pyramid can be built from a given bottom row and a set of allowed transitions.

        :param bottom: The bottom row of the pyramid as a string.
        :param allowed: A list of strings, where each string represents an allowed transition (e.g., "ABC" means A and B can form C).
        :return: True if a pyramid can be built, False otherwise.
        """
        transitionMap = defaultdict(list)
        for pattern in allowed:
            transitionMap[pattern[:2]].append(pattern[2])

        memo = {}

        def canBuild(row):
            if len(row) == 1:
                return True
            if row in memo:
                return memo[row]

            def backtrack(idx, nextRow):
                if idx == len(row) - 1:
                    return canBuild("".join(nextRow))

                key = row[idx:idx + 2]
                if key in transitionMap:
                    for val in transitionMap[key]:
                        nextRow.append(val)
                        if backtrack(idx + 1, nextRow):
                            return True
                        nextRow.pop()
                return False

            result = backtrack(0, [])
            memo[row] = result
            return result

        return canBuild(bottom)