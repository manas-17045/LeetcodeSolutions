# Leetcode 3948: Lexicographically Maximum MEX Array
# https://leetcode.com/problems/lexicographically-maximum-mex-array/
# Solved on 14th of June, 2026
class Solution:
    def maximumMEX(self, nums: list[int]) -> list[int]:
        """
        Finds the lexicographically maximum MEX array by greedily partitioning the input.

        :param nums: A list of non-negative integers.
        :return: A list of integers representing the lexicographically largest sequence of MEX values.
        """

        maxVal = max(nums) + 2
        freqList = [0] * maxVal

        for num in nums:
            freqList[num] += 1

        suffixMex = 0
        while freqList[suffixMex] > 0:
            suffixMex += 1

        resultArray = []
        seenGen = [0] * maxVal
        currGen = 1

        targetMex = suffixMex
        missingCount = targetMex

        for num in nums:
            freqList[num] -= 1

            if num < targetMex and seenGen[num] != currGen:
                seenGen[num] = currGen
                missingCount -= 1

            if num < suffixMex and freqList[num] == 0:
                suffixMex = num

            if missingCount == 0:
                resultArray.append(targetMex)
                targetMex = suffixMex
                missingCount = targetMex
                currGen += 1

        return resultArray