# Leetcode 1263: Minimum Moves to Move a Box to Their Target Location
# https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/
# Solved on 25th of September, 2025
import collections


class Solution:
    def minPushBox(self, grid: list[list[str]]) -> int:
        """
        Calculates the minimum number of pushes required to move a box to a target location.

        Args:
            grid (list[list[str]]): A 2D grid representing the game board.
                                    '#' denotes a wall, '.' denotes a floor,
                                    'B' denotes the box, 'S' denotes the player,
                                    'T' denotes the target location.
        Returns:
            int: The minimum number of pushes required. Returns -1 if the box cannot be moved to the target.
        """
        numRows = len(grid)
        numCols = len(grid[0])

        startBoxPos = None
        startPlayerPos = None
        targetPos = None

        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == 'B':
                    startBoxPos = (r, c)
                elif grid[r][c] == 'S':
                    startPlayerPos = (r, c)
                elif grid[r][c] == 'T':
                    targetPos = (r, c)

        initialState = (startBoxPos[0], startBoxPos[1], startPlayerPos[0], startPlayerPos[1])
        distances = {initialState: 0}
        queue = collections.deque([initialState])

        while queue:
            boxRow, boxCol, playerRow, playerCol = queue.popleft()

            if (boxRow, boxCol) == targetPos:
                return distances[(boxRow, boxCol, playerRow, playerCol)]

            currentPushes = distances[(boxRow, boxCol, playerRow, playerCol)]

            # Player moves without pushing (cost 0)
            for dRow, dCol in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newPlayerRow = playerRow + dRow
                newPlayerCol = playerCol + dCol

                if not (0 <= newPlayerRow < numRows and 0 <= newPlayerCol < numCols and grid[newPlayerRow][
                    newPlayerCol] != '#'):
                    continue

                if newPlayerRow == boxRow and newPlayerCol == boxCol:
                    continue

                newState = (boxRow, boxCol, newPlayerRow, newPlayerCol)
                if newState not in distances:
                    distances[newState] = currentPushes
                    queue.appendleft(newState)

            # Player pushes the box (cost 1)
            if abs(playerRow - boxRow) + abs(playerCol - boxCol) == 1:
                pushDirectionRow = boxRow - playerRow
                pushDirectionCol = boxCol - playerCol

                newBoxRow = boxRow + pushDirectionRow
                newBoxCol = boxCol + pushDirectionCol

                if not (0 <= newBoxRow < numRows and 0 <= newBoxCol < numCols and grid[newBoxRow][newBoxCol] != '#'):
                    continue

                newPlayerPosAfterPush = (boxRow, boxCol)

                newState = (newBoxRow, newBoxCol, newPlayerPosAfterPush[0], newPlayerPosAfterPush[1])
                newPushes = currentPushes + 1

                if newState not in distances or distances[newState] > newPushes:
                    distances[newState] = newPushes
                    queue.append(newState)

            return -1