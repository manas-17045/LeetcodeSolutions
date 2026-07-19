# Leetcode 3976: Maximum Subarray Sum After Multiplier
# https://leetcode.com/problems/maximum-subarray-sum-after-multiplier/
# Solved on 19th of July, 2026
class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        """
        Finds the maximum subarray sum after applying at most one multiplier operation.
        
        Args:
            nums: The input array.
            k: The multiplier.
            
        Returns:
            The maximum subarray sum.
        """
        currentUnop = nums[0]
        currentMul = nums[0] * k
        currentDiv = int(nums[0] / k)
        currentPost = -float('inf')
        maxSum = max(currentUnop, currentMul, currentDiv)

        for i in range(1, len(nums)):
            num = nums[i]
            nextUnop = max(0, currentUnop) + num
            nextMul = max(0, currentUnop, currentMul) + num * k
            nextDiv = max(0, currentUnop, currentDiv) + int(num / k)
            nextPost = max(currentMul, currentDiv, currentPost) + num

            currentUnop = nextUnop
            currentMul = nextMul
            currentDiv = nextDiv
            currentPost = nextPost

            maxSum = max(maxSum, currentUnop, currentMul, currentDiv, currentPost)

        return maxSum