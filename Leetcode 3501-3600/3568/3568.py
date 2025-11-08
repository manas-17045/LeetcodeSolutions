# Leetcode 3568: Minimum Moves to Clean the Classroom
# https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/
# Solved on 8th of November, 2025
import collections


class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        """
        Calculates the minimum number of moves required to clean all litter in the classroom.

        Args:
            classroom: A list of strings representing the classroom grid.
            energy: The initial energy of the robot.

        Returns:
            The minimum number of moves to clean all litter, or -1 if it's impossible.
        """
        numRows = len(classroom)
        numCols = len(classroom[0])
        litterCoords = {}
        startRow, startCol = -1, -1
        litterCount = 0

        for r in range(numRows):
            for c in range(numCols):
                if classroom[r][c] == 'S':
                    startRow, startCol = r, c
                elif classroom[r][c] == 'L':
                    litterCoords[(r, c)] = litterCount
                    litterCount += 1

        if litterCount == 0:
            return 0

        targetMask = (1 << litterCount) - 1

        queue = collections.deque()
        queue.append((startRow, startCol, 0, energy))

        visited = {}
        visited[(startRow, startCol, 0)] = energy

        currMoves = 0

        while queue:
            levelSize = len(queue)
            for _ in range(levelSize):
                r, c, currMask, currEnergy = queue.popleft()

                if currMask == targetMask:
                    return currMoves

                energyOnMove = -1
                if currEnergy > 0:
                    energyOnMove = currEnergy
                elif currEnergy == 0 and classroom[r][c] == 'R':
                    energyOnMove = energy

                if energyOnMove == -1:
                    continue

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nextRow, nextCol = r + dr, c + dc

                    if 0 <= nextRow < numRows and 0 <= nextCol < numCols and classroom[nextRow][nextCol] != 'X':
                        nextEnergy = energyOnMove - 1
                        nextMask = currMask
                        cellType = classroom[nextRow][nextCol]

                        if cellType == 'R':
                            nextEnergy = energy
                        elif cellType == 'L':
                            litterIndex = litterCoords.get((nextRow, nextCol))
                            if litterIndex is not None:
                                nextMask = currMask | (1 << litterIndex)

                        nextState = (nextRow, nextCol, nextMask)
                        if nextState not in visited or visited[nextState] < nextEnergy:
                            visited[nextState] = nextEnergy
                            queue.append((nextRow, nextCol, nextMask, nextEnergy))

            currMoves += 1

        return -1