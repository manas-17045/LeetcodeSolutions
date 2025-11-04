# Leetcode 3318: Find X-Sum of All K-Long Subarrays I
# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/
# Solved on 4th of November, 2025
class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        """
        Calculates the X-sum for all K-long subarrays in the given list of numbers.

        Args:
            nums (list[int]): The input list of integers.
            k (int): The length of the subarrays.
            x (int): The number of most frequent distinct elements to consider for the X-sum.

        Returns:
            list[int]: A list containing the X-sum for each K-long subarray.
        """
        def getXSum(subarray: list[int], xVal: int) -> int:

            counts = {}
            for num in subarray:
                counts[num] = counts.get(num, 0) + 1

            distinctCount = len(counts)

            if distinctCount < xVal:
                return sum(subarray)

            sortedItems = sorted(counts.items(), key=lambda item: (item[1], item[0]), reverse=True)

            topXElements = set()
            for i in range(xVal):
                topXElements.add(sortedItems[i][0])

            currentSum = 0
            for num in subarray:
                if num in topXElements:
                    currentSum += num

            return currentSum

        numLength = len(nums)
        answer = []

        for i in range(numLength - k + 1):
            subarray = nums[i:(i + k)]
            currentXSum = getXSum(subarray, x)
            answer.append(currentXSum)

        return answer