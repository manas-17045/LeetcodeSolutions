# Leetcode 3994: Minimum Adjacent Swaps to Partition Array
# https://leetcode.com/problems/minimum-adjacent-swaps-to-partition-array/
# Solved on 15th of August, 2026
class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        """
        Calculates the minimum number of adjacent swaps required to partition the array.
        
        :param nums: The array to partition.
        :param a: The lower bound of the middle partition.
        :param b: The upper bound of the middle partition.
        :return: The minimum number of adjacent swaps required to partition the array.
        """
        modVal = 1000000007
        totalSwaps = 0
        countMiddle = 0
        countRight = 0

        for currentNum in nums:
            if currentNum < a:
                totalSwaps = (totalSwaps + countMiddle + countRight) % modVal
            elif currentNum <= b:
                totalSwaps = (totalSwaps + countRight) % modVal
                countMiddle += 1
            else:
                countRight += 1

        return totalSwaps