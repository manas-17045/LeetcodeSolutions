# Leetcode 3234: Count the Number of Substrings With Dominant Ones
# https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/
# Solved on 15th of November, 2025
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        Counts the number of substrings where the count of '1's is greater than or equal to the square of the count of '0's.

        Args:
            s (str): The input binary string.
        Returns:
            int: The total number of dominant substrings.
        """
        n = len(s)
        totalSubstrings = 0
        currentOnes = 0
        zeroIndices = []

        for i in range(n):
            if s[i] == '1':
                currentOnes += 1
            else:
                totalSubstrings += currentOnes * (currentOnes + 1) // 2
                currentOnes = 0
                zeroIndices.append(i)

        totalSubstrings += currentOnes * (currentOnes + 1) // 2

        zerosCount = len(zeroIndices)
        maxZeros = int(n ** 0.5)

        for z in range(1, maxZeros + 1):
            requiredOnesSquare = z * z
            for i in range(zerosCount - z + 1):
                startZeroIndex = zeroIndices[i]
                endZeroIndex = zeroIndices[i + z - 1]

                prevZeroIndex = zeroIndices[i - 1] if i > 0 else -1
                nextZeroIndex = zeroIndices[i + z] if i + z < zerosCount else n

                leftOnes = startZeroIndex - prevZeroIndex - 1
                rightOnes = nextZeroIndex - endZeroIndex - 1

                onesBetween = (endZeroIndex - startZeroIndex + 1) - z

                requiredMoreOnes = requiredOnesSquare - onesBetween

                totalSubstrings += self.countValidPairs(leftOnes, rightOnes, requiredMoreOnes)

        return totalSubstrings

    def countValidPairs(self, left: int, right: int, required: int) -> int:
        if required <= 0:
            return (left + 1) * (right + 1)

        count = 0

        startLi1 = required
        endLi1 = left
        if startLi1 <= endLi1:
            numTerms1 = endLi1 - startLi1 + 1
            count += numTerms1 * (right + 1)

        startLi2 = 0
        endLi2 = min(left, required - 1)
        if startLi2 <= endLi2:
            minValidLi = max(startLi2, required - right - 1)
            if minValidLi <= endLi2:
                numTerms2 = endLi2 - minValidLi + 1
                firstTerm = right - required + 1 + minValidLi
                lastTerm = right - required + 1 + endLi2
                count += numTerms2 * (firstTerm + lastTerm) // 2

        return count