# Leetcode 3315: Construct the Minimum Bitwise Array II
# https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/
# Solved on 14th of October, 2025
class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        """
        Constructs an array where each element is the minimum possible value obtained by
        flipping at most one bit of the corresponding element in the input array.

        :param nums: A list of integers.
        :return: A list of integers where each element is the minimum bitwise value.
        """
        resultArray = []
        for currentNum in nums:
            if currentNum == 2:
                resultArray.append(-1)
            else:
                tempVal = currentNum + 1
                leastSignificantBitVal = tempVal & -tempVal
                flipMask = leastSignificantBitVal >> 1
                minVal = currentNum ^ flipMask
                resultArray.append(minVal)

        return resultArray