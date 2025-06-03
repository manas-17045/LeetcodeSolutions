# Leetcode 1298: Maximum Candies You Can Get from Boxes
# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/
# Solved on 3rd of June, 2025
from collections import deque


class Solution:
    def maxCandies(self, status: list[int], candies: list[int], keys: list[list[int]], containedBoxes: list[list[int]], initialBoxes: list[int]) -> int:
        """
        Calculates the maximum number of candies you can collect from a set of boxes.

        You start with a set of initial boxes. To open a box and collect its candies,
        you either need to have the box's status to be 1 (initially openable) or have a key
        for that box. Opening a box gives you its candies, potentially keys for other
        boxes, and potentially other boxes.

        Args:
            status: A list of integers where status[i] is 1 if box i is initially openable, and 0 otherwise.
            candies: A list of integers where candies[i] is the number of candies in box i.
            keys: A list of lists where keys[i] is a list of box indices for which box i contains a key.
            containedBoxes: A list of lists where containedBoxes[i] is a list of box indices contained within box i.
            initialBoxes: A list of integers representing the indices of the boxes you initially have.
        """
        n = len(status)

        totalCandiesCollected = 0

        hasKeyForBox = [False] * n
        weHaveThisBox = [False] * n
        processedBox = [False] * n

        queue = deque()

        for boxIdx in initialBoxes:
            weHaveThisBox[boxIdx] = True
            if status[boxIdx] == 1:
                if not processedBox[boxIdx]:
                    queue.append(boxIdx)
                    processedBox[boxIdx] = True

        while queue:
            currentBoxIdx = queue.popleft()

            totalCandiesCollected += candies[currentBoxIdx]

            for keyForBoxIdx in keys[currentBoxIdx]:
                hasKeyForBox[keyForBoxIdx] = True

                if weHaveThisBox[keyForBoxIdx] and status[keyForBoxIdx] == 0 and not processedBox[keyForBoxIdx]:
                    queue.append(keyForBoxIdx)
                    processedBox[keyForBoxIdx] = True

            for newFoundBoxIdx in containedBoxes[currentBoxIdx]:
                weHaveThisBox[newFoundBoxIdx] = True

                isOpenableNow = (status[newFoundBoxIdx] == 1) or (hasKeyForBox[newFoundBoxIdx])

                if isOpenableNow and not processedBox[newFoundBoxIdx]:
                    queue.append(newFoundBoxIdx)
                    processedBox[newFoundBoxIdx] = True

        return totalCandiesCollected