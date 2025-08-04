# Leetcode 2968: Apply Operations to Maximize Frequency Score
# https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/
# Solved on 4th of August, 2025
class Solution:
    def maxFrequencyScore(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum frequency score achievable from a list of numbers.
        The frequency score is the maximum length of a subarray where all elements
        can be made equal to the median of that subarray by performing operations,
        with a total cost not exceeding 'k'.
        :param nums: A list of integers.
        :param k: The maximum allowed cost for operations.
        :return: The maximum frequency score.
        """
        nums.sort()
        n = len(nums)
        
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        left = 0
        maxScore = 0
        
        for right in range(n):
            medianIndex = left + (right - left) // 2
            medianVal = nums[medianIndex]
            
            cost = ((medianVal * (medianIndex - left)) - (prefixSum[medianIndex] - prefixSum[left]) +
                    (prefixSum[right + 1] - prefixSum[medianIndex + 1]) - (medianVal * (right - medianIndex)))

            while cost > k:
                left += 1
                medianIndex = left + (right - left) // 2
                medianVal = nums[medianIndex]
                
                cost = ((medianVal * (medianIndex - left)) - (prefixSum[medianIndex] - prefixSum[left]) +
                        (prefixSum[right + 1] - prefixSum[medianIndex + 1]) - (medianVal * (right - medianIndex)))

            currentScore = right - left + 1
            if currentScore > maxScore:
                maxScore = currentScore
                
        return maxScore