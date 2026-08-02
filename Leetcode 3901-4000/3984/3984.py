# Leetcode 3984: Divisible Game
# https://leetcode.com/problems/divisible-game/
# Solved on 2nd of August, 2026
class Solution:
    def divisibleGame(self, nums: list[int]) -> int:
        """
        Finds the value of k that maximizes the expression (maxScoreDiff * k) % 1000000007,
        where maxScoreDiff is the maximum subarray sum of the array obtained by
        replacing each element in nums with either the element itself if it is
        divisible by k or the negative of the element if it is not divisible by k.

        Args:
            nums (list[int]): The input array of integers.

        Returns:
            int: The value of k that maximizes the expression (maxScoreDiff * k) % 1000000007.
        """
        modVal = 1000000007
        candidateKeys = {2}

        for num in nums:
            tempNum = num
            factor = 2
            while factor * factor <= tempNum:
                if tempNum % factor == 0:
                    candidateKeys.add(factor)
                    while tempNum % factor == 0:
                        tempNum //= factor
                factor += 1
            if tempNum > 1:
                candidateKeys.add(tempNum)

        maxScoreDiff = float("-inf")
        bestK = 2

        for k in sorted(candidateKeys):
            currentSum = nums[0] if nums[0] % k == 0 else -nums[0]
            maxSum = currentSum
            for i in range(1, len(nums)):
                val = nums[i] if nums[i] % k == 0 else -nums[i]
                currentSum = val if currentSum < 0 else currentSum + val
                if currentSum > maxSum:
                    maxSum = currentSum

            if maxSum > maxScoreDiff:
                maxScoreDiff = maxSum
                bestK = k

        return (maxScoreDiff * bestK) % modVal