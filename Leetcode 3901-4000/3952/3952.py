# Leetcode 3952: Maximum Total Value of Covered Indices
# https://leetcode.com/problems/maximum-total-value-of-covered-indices/
# Solved on 21st of June, 2026
class Solution:
    def maxTotal(self, nums: list[int], s: str) -> int:
        """
        Calculates the maximum total value of covered indices.
        
        :param nums: The array of values.
        :param s: The string indicating covered indices.
        :return: The maximum total value of covered indices.
        """
        numElements = len(nums)

        totalValue = 0
        currentIndex = 0

        while currentIndex < numElements:
            if s[currentIndex] == '1':
                leftIndex = currentIndex
                while currentIndex < numElements and s[currentIndex] == '1':
                    currentIndex += 1
                
                rightIndex = currentIndex - 1
                if leftIndex == 0:
                    totalValue += sum(nums[0 : rightIndex + 1])
                else:
                    totalValue += sum(nums[leftIndex - 1 : rightIndex + 1]) - min(nums[leftIndex - 1 : rightIndex + 1])
            else:
                currentIndex += 1

        return totalValue