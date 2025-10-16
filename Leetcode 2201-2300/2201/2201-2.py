# Leetcode 2201: Count Artifacts Thant Can Be Extracted
# https://leetcode.com/problems/count-artifacts-that-can-be-extracted/
# Solved on 16th of October, 2025
class Solution:
    def digArtifacts(self, n: int, artifacts: list[list[int]], dig: list[list[int]]) -> int:
        """
        Calculates the number of artifacts that can be fully extracted given a grid size,
        a list of artifacts' coordinates, and a list of dug cells.

        :param n: The size of the n x n grid.
        :param artifacts: A list of artifacts, where each artifact is defined by [r1, c1, r2, c2]
                          representing its top-left and bottom-right coordinates.
        :param dig: A list of dug cells, where each cell is defined by [r, c].
        :return: The total number of fully extracted artifacts.
        """
        # Store excavated cells in a set of tuples
        dug = {(r, c) for r, c in dig}

        extracted = 0
        for r1, c1, r2, c2 in artifacts:
            # Check every cell in the artifact's rectangle is dug
            fully_dug = True
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if (r, c) not in dug:
                        fully_dug = False
                        break

                if not fully_dug:
                    break

            if fully_dug:
                extracted += 1

        return extracted