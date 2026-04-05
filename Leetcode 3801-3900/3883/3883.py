# Leetcode 3883: Count Non Decreasing Arrays With Given Digit Sums
# https://leetcode.com/problems/coun-non-decreasing-arrays-with-given-digit-sums/
# Solved on 5th of April, 2026
class Solution:
    def countArrays(self, digitSum: list[int]) -> int:
        """
        Calculates the number of non-decreasing arrays where each element's digit sum matches the given list.

        :param digitSum: A list of integers representing the required digit sum for each element in the array.
        :return: The total number of valid non-decreasing arrays modulo 10^9 + 7.
        """
        modValue = 10**9 + 7
        maxVal = 5000

        validNums = [[] for _ in range(51)]
        for num in range(maxVal + 1):
            temp = num
            currentSum = 0
            while temp > 0:
                currentSum += temp % 10
                temp //= 10
            if currentSum <= 50:
                validNums[currentSum].append(num)

        dpState = [0] * (maxVal + 1)
        firstTarget = digitSum[0]
        for num in validNums[firstTarget]:
            dpState[num] = 1

        for i in range(1, len(digitSum)):
            targetSum = digitSum[i]
            prefixSum = [0] * (maxVal + 1)
            prefixSum[0] = dpState[0]
            for j in range(1, maxVal + 1):
                prefixSum[j] = (prefixSum[j - 1] + dpState[j]) % modValue

            nextDpState = [0] * (maxVal + 1)
            for num in validNums[targetSum]:
                nextDpState[num] = prefixSum[num]
            dpState = nextDpState

        totalArrays = 0
        for count in dpState:
            totalArrays = (totalArrays + count) % modValue

        return totalArrays