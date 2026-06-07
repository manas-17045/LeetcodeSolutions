# Leetcode 3942: Minimum Operations to Sort a Permutation
# https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/
# Solved on 7th of June, 2026
import collections


class Solution:
    def minOperations(self, nums: list[int]) -> int:

        n = len(nums)
        zeroIndex = nums.index(0)
        isTargetZero = True
        for i in range(n):
            if nums[(zeroIndex + i) % n] != i:
                isTargetZero = False
                break

        reversedNums = nums[::-1]
        revZeroIndex = reversedNums.index(0)
        isTargetOne = True
        for i in range(n):
            if reversedNums[(revZeroIndex + i) % n] != i:
                isTargetOne = False
                break

        if not isTargetZero and not isTargetOne:
            return -1

        queue = collections.deque([(0, 0, 0)])
        visited = [[False] * n for _ in range(2)]
        visited[0][0] = True

        while queue:
            currentType, currentShift, currentDist = queue.popleft()

            if (isTargetZero and currentType == 0 and currentShift == zeroIndex) or \
                    (isTargetOne and currentType == 1 and currentShift == revZeroIndex):
                return currentDist

            nextShiftOne = (currentShift + 1) % n
            if not visited[currentType][nextShiftOne]:
                visited[currentType][nextShiftOne] = True
                queue.append((currentType, nextShiftOne, currentDist + 1))

            nextTypeTwo = 1 - currentType
            nextShiftTwo = (n - currentShift) % n
            if not visited[nextTypeTwo][nextShiftTwo]:
                visited[nextTypeTwo][nextShiftTwo] = True
                queue.append((nextTypeTwo, nextShiftTwo, currentDist + 1))

        return -1