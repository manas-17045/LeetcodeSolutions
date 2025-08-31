# Leetcode 1345: Jump Game IV
# https://leetcode.com/problems/jump-game-iv/
# Solved on 31st of August, 2025
import collections


class Solution:
    def minJumps(self, arr: list[int]) -> int:
        """
        Calculates the minimum number of jumps required to reach the last index of the array.

        Args:
            arr (list[int]): The input array of integers.
        Returns:
            int: The minimum number of jumps.
        """
        n = len(arr)
        if n < 1 or n == 1:
            return 0

        valueIndices = collections.defaultdict(list)
        for i, val in enumerate(arr):
            valueIndices[val].append(i)

        q = collections.deque([(0, 0)])
        visited = {0}

        while q:
            currentIndex, steps = q.popleft()

            if currentIndex == n - 1:
                return steps

            currentVal = arr[currentIndex]
            if currentVal in valueIndices:
                for nextIndex in valueIndices[currentVal]:
                    if nextIndex not in visited:
                        visited.add(nextIndex)
                        q.append((nextIndex, steps + 1))
                del valueIndices[currentVal]

            nextIndexPlus = currentIndex + 1
            if nextIndexPlus < n and nextIndexPlus not in visited:
                visited.add(nextIndexPlus)
                q.append((nextIndexPlus, steps + 1))

            nextIndexMinus = currentIndex - 1
            if nextIndexMinus >= 0 and nextIndexMinus not in visited:
                visited.add(nextIndexMinus)
                q.append((nextIndexMinus, steps + 1))

        return -1