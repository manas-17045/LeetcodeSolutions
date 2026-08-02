# Leetcode 3985: Palindromic Subarray Sum
# https://leetcode.com/problems/palindromic-subarray-sum/
# Solved on 2nd of August, 2026
class Solution:
    def getSum(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of a palindromic subarray.

        Args:
            nums: The input array.

        Returns:
            The maximum palindromic subarray sum.
        """
        modifiedNums = [-2, -1]

        for num in nums:
            modifiedNums.append(nums)
            modifiedNums.append(-1)

        modifiedNums.append(-3)

        n = len(modifiedNums)
        palindromeRadius = [0] * n
        center = 0
        rightBoundary = 0

        for i in range(1, n - 1):
            mirror = 2 * center - i

            if i < rightBoundary:
                palindromeRadius[i] = min(rightBoundary - i, palindromeRadius[mirror])

            while modifiedNums[i + 1 + palindromeRadius[i]] == modifiedNums[i - 1 - palindromeRadius[i]]:
                palindromeRadius[i] += 1

            if i + palindromeRadius[i] > rightBoundary:
                center = i
                rightBoundary = i + palindromeRadius[i]

        prefixSum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        maxSum = 0

        for i in range(1, n - 1):
            length = palindromeRadius[i]

            if length > 0:
                startIndex = (i - 1 - length) // 2
                currentSum = prefixSum[startIndex + length] - prefixSum[startIndex]

                if currentSum > maxSum:
                    maxSum = currentSum

        return maxSum