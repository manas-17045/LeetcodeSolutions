# Leetcode 1840: Maximum Building Height
# https://leetcode.com/problems/maximum-building-height/
# Solved on 22nd of July, 2025
class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        """
        Calculates the maximum possible height of any building given restrictions.
        :param n: The total number of buildings.
        :param restrictions: A list of [id, height] pairs representing restrictions on building heights.
        :return: The maximum possible height of any building.
        """
        allPoints = sorted(restrictions + [[1, 0]])

        # Add [1, 0] uf not present and remove duplicates.
        if not allPoints or allPoints[0][0] != 1:
            allPoints.insert(0, [1, 0])

        tempList = []
        if allPoints:
            tempList.append(allPoints[0])
            for i in range(1, len(allPoints)):
                if allPoints[i][0] != allPoints[i - 1][0]:
                    tempList.append(allPoints[i])
        allPoints = tempList

        # Left-to-right pass to enforce constraints
        for i in range(1, len(allPoints)):
            prevId, prevHeight = allPoints[i - 1]
            currId, currHeight = allPoints[i]
            allowedHeight = prevHeight + (currId - prevId)
            allPoints[i][1] = min(currHeight, allowedHeight)

        # Right-to-left pass to enforce constraints
        for i in range(len(allPoints) - 2, -1, -1):
            nextId, nextHeight = allPoints[i + 1]
            currId, currHeight = allPoints[i]
            allowedHeight = nextHeight + (nextId - currId)
            allPoints[i][1] = min(currHeight, allowedHeight)

        maxHeight = 0

        # Calculate max height between adjacent anchor points
        for i in range(len(allPoints) - 1):
            idOne, heightOne = allPoints[i]
            idTwo, heightTwo = allPoints[i + 1]

            peak = (heightOne + heightTwo + idTwo - idOne) // 2
            maxHeight = max(maxHeight, peak)

        # Calculate max height in the last segment
        lastId, lastHeight = allPoints[-1]
        maxHeight = max(maxHeight, lastHeight + (n - lastId))

        return maxHeight