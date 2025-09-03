# Leetcode 2829: Determine the Minimum Sum of a k-avoiding Array
# https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/
# Solved on 3rd of September, 2025
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        """
        Determines the minimum sum of a k-avoiding array.

        Args:
            n (int): The desired length of the array.
            k (int): The integer for the k-avoiding condition (no two distinct elements sum to k).
        Returns:
            int: The minimum possible sum of a k-avoiding array of length n.
        """
        addedNumbers = set()
        currentSum = 0
        currentNum = 1
        while len(addedNumbers) < n:
            if (k - currentNum) not in addedNumbers:
                addedNumbers.add(currentNum)
                currentSum += currentNum
            currentNum += 1
        return currentSum