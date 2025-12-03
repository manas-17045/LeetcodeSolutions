# Leetcode 3597: Partition String
# https://leetcode.com/problems/partition-string/
# Solved on 3rd of December, 2025
class Solution:
    def partitionString(self, s: str) -> list[str]:
        """
        Partitions the input string `s` into a list of non-overlapping substrings.

        :param s: The input string to be partitioned.
        :return: A list of strings representing the partitioned segments.
        """
        seenSegments = set()
        result = []
        currentSegment = ""

        for char in s:
            currentSegment += char

            if currentSegment not in seenSegments:
                seenSegments.add(currentSegment)
                result.append(currentSegment)
                currentSegment = ""

        return result