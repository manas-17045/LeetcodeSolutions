# Leetcode 3551: Minimum Swaps to Sort by Digit Sum
# https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/
# Solved on 28th of November, 2025
class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of swaps required to sort the array `nums` based on the digit sum of its elements.
        :param nums: A list of integers.
        :return: The minimum number of swaps.
        """
        def getDigitSum(num):
            currentSum = 0
            while num > 0:
                currentSum += num % 10
                num //= 10

            return currentSum

        n = len(nums)
        elements = []
        for i in range(n):
            val = nums[i]
            elements.append((getDigitSum(val), val. i))

        elements.sort()

        targetPos = [0] * n
        for i in range(n):
            originIdx = elements[i][2]
            targetPos[originIdx] = i

        visited = [False] * n
        totalSwaps = 0

        for i in range(n):
            if visited[i] or targetPos[i] == i:
                continue

            cycleLen = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = targetPos[curr]
                cycleLen += 1

            if cycleLen > 1:
                totalSwaps += cycleLen - 1

        return totalSwaps