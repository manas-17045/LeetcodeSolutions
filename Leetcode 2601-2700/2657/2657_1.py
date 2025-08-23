# Leetcode 2657: Find the Prefix Common Array of Two Arrays
# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/
# Solved on 23rd of August, 2025
class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        """
        Finds the prefix common array of two arrays A and B.

        Args:
            A (list[int]): The first input array.
            B (list[int]): The second input array.

        Returns:
            list[int]: A list where resultArray[i] is the number of common elements
                       in the prefix A[0...i] and B[0...i].
        """
        n = len(A)
        resultArray = []
        commonCount = 0
        freqA = [0] * (n + 1)
        freqB = [0] * (n + 1)

        for i in range(n):
            valA = A[i]
            valB = B[i]

            if valA == valB:
                commonCount += 1
            else:
                if freqB[valA] > 0:
                    commonCount += 1
                if freqA[valB] > 0:
                    commonCount += 1

            freqA[valA] = 1
            freqB[valB] = 1

            resultArray.append(commonCount)

        return resultArray