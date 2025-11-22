# Leetcode 2593: Find Score of an Array After Marking All Elements
# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/
# Solved on 22nd of November, 2025
class Solution:
    def findScore(self, nums: list[int]) -> int:
        """
        Calculates the score of an array after marking elements.

        Args:
            nums (list[int]): The input array of integers.
        Returns:
            int: The total score.
        """
        length = len(nums)
        sortedArray = []
        for i in range(length):
            sortedArray.append((nums[i], i))

        sortedArray.sort()

        isMarked = [False] * length
        finalScore = 0

        for value, index in sortedArray:
            if not isMarked[index]:
                finalScore += value
                isMarked[index] = True

                if index > 0:
                    isMarked[index - 1] = True

                if index < length - 1:
                    isMarked[index + 1] = True

        return finalScore