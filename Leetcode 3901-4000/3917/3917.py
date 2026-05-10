# Leetcode 3917: Count Indices With Opposite Parity
# https://leetcode.com/problems/count-indices-with-opposite-parity/
# Solved on 10th of May, 2026
class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        """
        Calculates the number of elements to the right of each index that have the opposite parity.

        Args:
            nums (list[int]): A list of integers to process.
        Returns:
            list[int]: A list where each element at index i is the count of elements with opposite parity in nums[i+1:].
        """
        oddCount = 0
        evenCount = 0
        n = len(nums)

        for i in range(n - 1, -1, -1):
            currentNum = nums[i]
            if currentNum % 2 == 0:
                nums[i] = oddCount
                evenCount += 1
            else:
                nums[i] = evenCount
                oddCount += 1

        return nums