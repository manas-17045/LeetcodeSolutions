# Leetcode 1850: Minimum Adjacent Swaps to Reach the Kth Smallest Number
# https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/
# Solved on 15th of November, 2025
class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        """
        Calculates the minimum number of adjacent swaps required to transform the original number
        into the k-th smallest number greater than the original number.
        :param num: A string representing the original number.
        :param k: An integer representing the k-th smallest number to reach.
        :return: The minimum number of adjacent swaps.
        """
        def nextPermutation(digitsList: list) -> None:
            length = len(digitsList)
            i = length - 2

            while i >= 0 and digitsList[i] >= digitsList[i + 1]:
                i -= 1

            if i == -1:
                digitsList.reverse()
                return

            j = length - 1
            while digitsList[j] <= digitsList[i]:
                j -= 1

            digitsList[i], digitsList[j] = digitsList[j], digitsList[i]

            left = i + 1
            right = length - 1
            while left < right:
                digitsList[left], digitsList[right] = digitsList[right], digitsList[left]
                left += 1
                right -= 1

        originalDigits = list(num)
        targetDigits = list(num)

        for _ in range(k):
            nextPermutation(targetDigits)

        n = len(originalDigits)
        totalSwaps = 0

        for i in range(n):
            if originalDigits[i] != targetDigits[i]:
                targetChar = targetDigits[i]
                j = i + 1

                while originalDigits[j] != targetChar:
                    j += 1

                swapsNeeded = j - i
                totalSwaps += swapsNeeded

                charToMove = originalDigits.pop(j)
                originalDigits.insert(i, charToMove)

        return totalSwaps