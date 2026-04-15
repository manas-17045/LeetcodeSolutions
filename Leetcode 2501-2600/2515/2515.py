# Leetcode 2515: Shortest Distance to Target String in a Circular Array
# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/
# Solved on 15th of April, 2026
class Solution:
    def closetTarget(self, words: list[str], target: str, startIndex: int) -> int:
        """
        Finds the shortest distance to the target string in a circular array.

        :param words: A list of strings representing the circular array.
        :param target: The string to search for in the array.
        :param startIndex: The starting index for the search.
        :return: The minimum distance to the target string, or -1 if not found.
        """
        minDistance = -1
        arrayLength = len(words)

        for i in range(arrayLength):
            if words[i] == target:
                forwardDistance = abs(i - startIndex)
                actualDistance = min(forwardDistance, arrayLength - forwardDistance)

                if minDistance == -1 or actualDistance < minDistance:
                    minDistance = actualDistance

        return minDistance