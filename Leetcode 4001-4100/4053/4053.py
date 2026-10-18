# Leetcode 4053: Minimum Operations to Make Every Element Palindromic
# https://leetcode.com/problems/minimum-operations-to-make-every-element-palindromic/
# Solved on 18th of October, 2026
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of operations required to make every element
        in the given integer list a positive palindrome by incrementing or
        decrementing elements by 2.

        Parameters:
            nums (list[int]): A list of positive integers.

        Returns:
            int: The minimum total number of operations required.
        """
        totalOps = 0

        for num in nums:
            if num < 10:
                continue

            numStr = str(num)
            length = len(numStr)
            parity = num & 1
            firstDigit = ord(numStr[0]) - 48

            lowDigit = firstDigit - 2 if (firstDigit & 1) == parity else firstDigit - 1
            if lowDigit >= 1:
                lowCand = (lowDigit + 1) * (10 ** (length - 1)) - 10 + lowDigit
            else:
                maxValidDigit = 8 + parity
                if length == 2:
                    lowCand = maxValidDigit
                else:
                    lowCand = (maxValidDigit + 1) * (10 ** (length - 2)) - 10 + maxValidDigit

            highDigit = firstDigit + 2 if (firstDigit & 1) == parity else firstDigit + 1
            if highDigit <= 9:
                highCand = highDigit * (10 ** (length - 1)) + highDigit
            else:
                minValidDigit = 2 - parity
                highCand = minValidDigit * (10 ** length) + minValidDigit

            minDiff = num - lowCand
            highDiff = highCand - num
            if highDiff < minDiff:
                minDiff = highDiff

            if (firstDigit & 1) == parity:
                halfLen = (length + 1) // 2
                prefix = int(numStr[:halfLen])

                for candPrefix in (prefix - 1, prefix, prefix + 1):
                    candStr = str(candPrefix)
                    if len(candStr) == halfLen:
                        if length & 1:
                            palStr = candStr + candStr[:-1][::-1]
                        else:
                            palStr = candStr + candStr[::-1]

                        palVal = int(palStr)
                        if (palVal & 1) == parity:
                            diff = abs(num - palVal)
                            if diff < minDiff:
                                minDiff = diff

            totalOps += minDiff // 2

        return totalOps