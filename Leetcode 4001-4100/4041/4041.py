# Leetcode 4041: Minimum Operations to Form Subset Sum II
# https://leetcode.com/problems/minimum-operations-to-form-subset-sum-ii/ 
# Solved on 3rd of October, 2026
class Solution:
    def minOperationns(self, nums: list[int], sum: int) -> int:
        """
        Generates all valid reachable values and their minimum operation costs for a given integer.
        
        Args:
            num (int): The initial element value from the array.
            targetSum (int): The maximum value limit to track reachable states.
            
        Returns:
            dict: A mapping of reachable values to their minimum required operations.
        """
        targetSum = sum
        infinity = float('inf')
        
        dp = [infinity] * (targetSum + 1)
        dp[0] = 0
        validSums = {0}

        for num in nums:
            reachable = self.getReachableValues(num, targetSum)
            nextDp = list(dp)
            nextValidSums = set(validSums)

            for currentSum in validSums:
                currentCost = dp[currentSum]

                for val, cost in reachable.items():
                    nextSum = currentSum + cost

                    if nextSum <= targetSum:
                        newCost = currentCost + cost

                        if newCost < nextDp[nextSum]:
                            nextDp[nextSum] = newCost
                            nextValidSums.add(nextSum)

            dp = nextDp
            validSums = nextValidSums

        return dp[targetSum] if dp[targetSum] != infinity else -1

    def getReachableValues(self, num: int, targetSum: int) -> dict:

        reachable = {}
        divCount = 0
        currentVal = num
        
        while True:
            multCount = 0
            tempVal = currentVal
            
            while tempVal <= targetSum:
                cost = divCount + multCount
                
                if tempVal > 0:
                    if tempVal not in reachable or cost < reachable[tempVal]:
                        reachable[tempVal] = cost
                        
                if tempVal == 0:
                    break
                    
                tempVal *= 2
                multCount += 1
                
            if currentVal == 0:
                break
                
            currentVal //= 2
            divCount += 1
            
        return reachable