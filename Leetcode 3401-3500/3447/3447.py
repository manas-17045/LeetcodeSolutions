# Leetcode 3447: Assign Elements to Groups with Constraints
# https://leetcode.com/problems/assign-elements-to-groups-with-constraints/
# Solved on 23rd of October, 2025
class Solution:
    def assignElements(self, groups: list[int], elements: list[int]) -> list[int]:

        numElements = len(elements)
        maxVal = 100001

        firstIndex = [numElements] * maxVal
        for j in range(numElements):
            val = elements[j]
            if firstIndex[val] == numElements:
                firstIndex[val] = j

        minDivisorIndex = [numElements] * maxVal
        for val in range(1, maxVal):
            idx = firstIndex[val]
            if idx == numElements:
                continue

            for multiple in range(val, maxVal, val):
                minDivisorIndex[multiple] = min(minDivisorIndex[multiple], idx)

        assigned = []
        for g in groups:
            idx = minDivisorIndex[g]
            assigned.append(idx if idx != numElements else -1)

        return assigned