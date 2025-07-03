# Leetcode 3287: Find the Maximum Sequence Value of Array
# https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/
# Solved on 3rd of July, 2025
class Solution:
    def maxValue(self, nums: list[int], k: int) -> int:
        """
        Finds the maximum sequence value of an array.

        The sequence value is defined as the bitwise OR of the first k elements
        XORed with the bitwise OR of the last k elements.

        Args:
            nums: A list of integers.
            k: An integer representing the number of elements for OR operations.
        """
        n = len(nums)

        prefixOrSums = [[set() for _ in range(k + 1)] for _ in range(n)]
        prefixOrSums[0][1] = {nums[0]}

        for i in range(1, n):
            for j in range(1, k + 1):
                prefixOrSums[i][j].update(prefixOrSums[i - 1][j])
                if j == 1:
                    prefixOrSums[i][j].add(nums[i])
                else:
                    for val in prefixOrSums[i - 1][j - 1]:
                        prefixOrSums[i][j].add(val | nums[i])

        suffixOrSums = [[set() for _ in range(k + 1)] for _ in range(n)]
        suffixOrSums[n - 1][1] = {nums[n - 1]}

        for i in range((n - 2), -1, -1):
            for j in range(1, k + 1):
                suffixOrSums[i][j].update(suffixOrSums[i + 1][j])
                if j == 1:
                    suffixOrSums[i][j].add(nums[i])
                else:
                    for val in suffixOrSums[i + 1][j - 1]:
                        suffixOrSums[i][j].add(val | nums[i])

        maxValue = 0
        BIT_LENGTH = 7

        for i in range((k - 1), (n - k)):
            firstHalfOrs = prefixOrSums[i][k]
            secondHalfOrs = suffixOrSums[i + 1][k]

            if not firstHalfOrs or not secondHalfOrs:
                continue

            trieRoot = {}
            for v2 in secondHalfOrs:
                node = trieRoot
                for bitPos in range(BIT_LENGTH - 1, -1, -1):
                    bit = (v2 >> bitPos) & 1
                    if bit not in node:
                        node[bit] = {}
                    node = node[bit]

            currentMax = 0
            for v1 in firstHalfOrs:
                node = trieRoot
                currentXor = 0
                for bitPos in range(BIT_LENGTH - 1, -1, -1):
                    bit = (v1 >> bitPos) & 1
                    oppositeBit = 1 - bit
                    if oppositeBit in node:
                        currentXor |= (1 << bitPos)
                        node = node[oppositeBit]
                    else:
                        node = node[bit]
                currentMax = max(currentMax, currentXor)

            maxValue = max(maxValue, currentMax)

        return maxValue