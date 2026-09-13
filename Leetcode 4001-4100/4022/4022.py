# Leetcode 4022: K-th Digit in Infinite String
# https://leetcode.com/problems/k-th-digit-in-infinite-string/
# Solved on 13th of September, 2026
class Solution:
    def kthDigit(self, k: int) -> int:
        """
        Finds the k-th digit of the infinite string formed by concatenated blocks.

        Parameters:
            k (int): The 1-based index of the digit to retrieve.

        Returns:
            int: The digit at the k-th position.
        """
        if k <= 9:
            return k

        lowVal = 1
        highVal = k
        targetBlock = 1
        while lowVal <= highVal:
            midVal = (lowVal + highVal) // 2
            if self.countDigits(10 * midVal + 9) >= k:
                targetBlock = midVal
                highVal = midVal - 1
            else:
                lowVal = midVal + 1

        digitsBefore = self.countDigits(10 * (targetBlock - 1) + 9)
        remainingDigits = k - digitsBefore
        digitLength = len(str(10 * targetBlock))
        blockOffset = remainingDigits - 1
        numberIndex = blockOffset // digitLength
        digitIndex = blockOffset % digitLength

        if targetBlock % 2 == 0:
            targetNumber = 10 * targetBlock + numberIndex
        else:
            targetNumber = 10 * targetBlock + (9 - numberIndex)

        return int(str(targetNumber)[digitIndex])

    def countDigits(self, maxVal: int) -> int:
        totalDigits = 0
        currentLength = 1
        rangeStart = 1
        
        while rangeStart <= maxVal:
            rangeEnd = rangeStart * 10 - 1
            totalDigits += (min(maxVal, rangeEnd) - rangeStart + 1) * currentLength
            rangeStart *= 10
            currentLength += 1

        return totalDigits