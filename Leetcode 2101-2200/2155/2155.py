# Leetcode 2155: All Divisions With the Highest Score of a Binary Array
# https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/
# Solved on 11th of November, 2025
class Solution:
    def maxScoreIndices(self, nums: list[int]) -> list[int]:
        """
        Calculates all division indices that result in the highest score.
        A division at index `i` means splitting the array into `nums[0...i-1]` and `nums[i...n-1]`.
        The score for a division is the number of zeros in the left part plus the number of ones in the right part.

        :param nums: A binary array (contains only 0s and 1s).
        :return: A list of all division indices that yield the maximum score.
                 The division index 0 means the left part is empty, and index n means the right part is empty.
        """
        n = len(nums)
        onesRight = nums.count(1)
        zerosLeft = 0

        currentScore = zerosLeft + onesRight
        maxScore = currentScore
        resultIndices = [0]

        for i in range(n):
            if nums[i] == 0:
                zerosLeft += 1
            else:
                onesRight -= 1

            currentScore = zerosLeft + onesRight
            divisionIndex = i + 1

            if currentScore > maxScore:
                maxScore = currentScore
                resultIndices = [divisionIndex]
            elif currentScore == maxScore:
                resultIndices.append(divisionIndex)

        return resultIndices