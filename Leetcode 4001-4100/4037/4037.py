# Leetcode 4037: Maximum Valid Split Positions II
# https://leetcode.com/problems/maximum-valid-split-positions-ii/
# Solved on 29th of September, 2026
import math


class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        """
        Calculates the maximum possible score of the array after optionally 
        removing at most one element. The score is defined as the number 
        of valid split positions where the greatest common divisor (GCD) 
        of the left part equals the GCD of the right part.
        
        Parameters:
            nums (list[int]): The input array of positive integers.
        
        Returns:
            int: The maximum number of valid split positions achievable.
        """
        n = len(nums)

        prefGcd = [0] * n
        prefGcd[0] = nums[0]
        for i in range(1, n):
            prefGcd[i] = math.gcd(prefGcd[i - 1], nums[i])

        suffGcd = [0] * n
        suffGcd[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffGcd[i] = math.gcd(suffGcd[i + 1], nums[i])

        maxScore = 0
        for i in range(n - 1):
            if prefGcd[i] == suffGcd[i + 1]:
                maxScore += 1

        candidates = {0, n - 1}
        for i in range(1, n):
            if prefGcd[i] != prefGcd[i - 1]:
                candidates.add(i)
        
        for i in range(n - 2, -1, -1):
            if suffGcd[i] != suffGcd[i + 1]:
                candidates.add(i)

        for c in candidates:
            score = 0

            rightGcd = suffGcd[c + 1] if c + 1 < n else 0
            for i in range(c - 1, -1, -1):
                if rightGcd != 0:
                    if prefGcd[i] == rightGcd:
                        score += 1
                rightGcd = math.gcd(nums[i], rightGcd) if rightGcd != 0 else nums[i]

            leftGcd = prefGcd[c - 1] if c - 1 >= 0 else 0
            for i in range(c + 1, n - 1):
                leftGcd = math.gcd(leftGcd, nums[i]) if leftGcd != 0 else nums[i]
                if leftGcd == suffGcd[i + 1]:
                    score += 1

            if score > maxScore:
                maxScore = score
                
        return maxScore