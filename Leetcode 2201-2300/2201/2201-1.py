# Leetcode 2201: Count Artifacts Thant Can Be Extracted
# https://leetcode.com/problems/count-artifacts-that-can-be-extracted/
# Solved on 16th of October, 2025
class Solution:
    def digArtifacts(self, n: int, artifacts: list[list[int]], dig: list[list[int]]) -> int:
        """
        Counts the number of artifacts that can be fully extracted.

        Args:
            n (int): The size of the n x n grid.
            artifacts (list[list[int]]): A list of artifacts, where each artifact is defined by its top-left (r1, c1)
                                         and bottom-right (r2, c2) coordinates.
            dig (list[list[int]]): A list of cells that have been dug, where each cell is represented by [r, c].
        Returns:
            int: The total number of artifacts that can be fully extracted.
        """

        dugCells = {tuple(cell) for cell in dig}
        extractedCount = 0

        for artifact in artifacts:
            isFullyDug = True
            r1, c1, r2, c2 = artifact

            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if (r, c) not in dugCells:
                        isFullyDug = False
                        break

                if not isFullyDug:
                    break

            if isFullyDug:
                extractedCount += 1

        return extractedCount