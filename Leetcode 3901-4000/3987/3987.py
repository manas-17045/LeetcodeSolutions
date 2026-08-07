# Leetcode 3987: Minimum Total Cost to Process All Elements
# https://leetcode.com/problems/minimum-total-cost-to-process-all-elements/
# Solved on 7th of August, 2026
class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum total cost to process all elements in an array.
        The cost is determined by the sum of the number of operations required for each element.
        
        Args:
            nums: The array of integers to process.
            k: The cost of a single operation.
        
        Returns:
            The minimum total cost to process all elements.
        """
        currentResources = k
        totalOperations = 0
        modValue = 10**9 + 7

        for num in nums:
            if currentResources < num:
                neededResources = num - currentResources
                requiredOps = (neededResources + k - 1) // k
                totalOperations += requiredOps
                currentResources += requiredOps * k
            currentResources -= num

        return (totalOperations * (totalOperations + 1) // 2) % modValue