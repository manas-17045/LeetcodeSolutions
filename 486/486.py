# Leetcode 486: Predict the Winner
# https://leetcode.com/problems/predict-the-winner/
# Solved on 1st of August, 2026
class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        """
        Determines if the first player can win in the given array.
        
        Args:
            nums (list[int]): The array of integers.
        
        Returns:
            bool: True if the first player can win, False otherwise.
        """
        numCount = len(nums)
        scoreDp = list(nums)
        for leftIndex in range(numCount - 1, -1, -1):
            for rightIndex in range(leftIndex + 1, numCount):
                scoreDp[rightIndex] = max(
                    nums[leftIndex] - scoreDp[rightIndex],
                    nums[rightIndex] - scoreDp[rightIndex - 1]
                )
                
        return scoreDp[numCount - 1] >= 0