# Leetcode 3980: Minimum Operations to Transform Binary String
# https://leetcode.com/problems/minimum-operations-to-transform-binary-string/
# Solved on 26th of July, 2026
class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        """
        Finds the minimum number of operations to transform s1 to s2.
        @param s1: The source binary string.
        @param s2: The target binary string.
        @return: The minimum number of operations to transform s1 to s2.
        """
        stringLength = len(s1)
        nextDpZero = 0 if s2[-1] == '0' else 1
        nextDpOne = 0 if s2[-1] == '1' else float('inf')

        for index in range(stringLength - 2, -1, -1):
            nextVal = s1[index + 1]
            targetVal = s2[index]

            if targetVal == '0':
                costOneForZero = nextDpOne if nextVal == '1' else nextDpZero
            else:
                costOneForZero = 1 + (nextDpOne if nextVal == '1' else nextDpZero)

            costTwoForZero = 2 + (1 if nextVal == '0' else 0) + (1 if targetVal == '1' else 0) + nextDpZero
            currentDpZero = min(costOneForZero, costTwoForZero)

            if targetVal == '1':
                costOneForOne = nextDpOne if nextVal == '1' else nextDpZero
            else:
                costOneForOne = float('inf')

            costTwoForOne = 1 + (1 if nextVal == '0' else 0) + (1 if targetVal == '1' else 0) + nextDpZero
            currentDpOne = min(costOneForOne, costTwoForOne)

            nextDpZero = currentDpZero
            nextDpOne = currentDpOne

        resultCost = nextDpOne if s1[0] == '1' else nextDpZero
        return resultCost if resultCost < float('inf') else -1