# Leetcode 4040: Minimum Operations to Form Subset Sum I
# https://leetcode.com/problems/minimum-operations-to-form-subset-sum-i/
# Solved on 2nd of October, 2026
class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        """
        Calculate the minimum operations required to obtain a subset of transformed elements
        whose sum is exactly equal to the target sum.

        Parameters:
            nums (list[int]): The initial list of integers.
            sum (int): The target subset sum to achieve.

        Returns:
            int: The minimum operations needed, or -1 if impossible.
        """
        targetSum = sum
        infinityCost = 10**9
        dpTable = [infinityCost] * (targetSum + 1)
        dpTable[0] = 0
        reachableSums = [0]
        candidateCache = {}

        for numVal in nums:
            if numVal not in candidateCache:
                candidateCache[numVal] = self.buildCandidates(numVal, targetSum)
            candidateList = candidateCache[numVal]

            nextDpTable = list(dpTable)
            for candVal, candCost in candidateList:
                maxPrevSum = targetSum - candVal
                for prevSum in reachableSums:
                    if prevSum > maxPrevSum:
                        break
                    currentCost = dpTable[prevSum] + candCost
                    newSum = prevSum + candVal
                    if currentCost < nextDpTable[newSum]:
                        nextDpTable[newSum] = currentCost

            newSumsAdded = False
            for sumVal in range(1, targetSum + 1):
                if nextDpTable[sumVal] < dpTable[sumVal]:
                    if dpTable[sumVal] == infinityCost:
                        reachableSums.append(sumVal)
                        newSumsAdded = True
                    dpTable[sumVal] = nextDpTable[sumVal]

            if newSumsAdded:
                reachableSums.sort()

            if dpTable[targetSum] == 0:
                return 0

        finalAnswer = dpTable[targetSum]
        return -1 if finalAnswer >= infinityCost else finalAnswer

    def buildCandidates(self, numVal: int, targetSum: int) -> list[tuple[int, int]]:

        candidateList = []
        if numVal <= targetSum:
            candidateList.append((numVal, 0))

        currentVal = numVal
        opCount = 0
        while currentVal > 1:
            currentVal //= 2
            opCount += 1
            if currentVal <= targetSum:
                candidateList.append((currentVal, opCount))

        currentVal = numVal
        opCount = 0
        while currentVal * 2 <= targetSum:
            currentVal *= 2
            opCount += 1
            candidateList.append((currentVal, opCount))

        return candidateList