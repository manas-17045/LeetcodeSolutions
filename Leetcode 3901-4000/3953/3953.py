# Leetcode 3953: Maximum Score with Co-Prime Element
# https://leetcode.com/problems/maximum-score-with-co-prime-element/
# Solved on 22nd of June, 2026
class Solution:
    def maxScore(self, nums: list[int], maxVal: int) -> int:
        """
        Calculates the maximum score with co-prime element.
        
        :param nums: The array of numbers.
        :param maxVal: The maximum value allowed.
        :return: The maximum score with co-prime element.
        """
        maxNum = max(max(nums), maxVal)

        mobius = [0] * (maxNum + 1)
        mobius[1] = 1
        primeList = []
        isPrime = [True] * (maxNum + 1)

        for i in range(2, maxNum + 1):
            if isPrime[i]:
                primeList.append(i)
                mobius[i] = -1
            for p in primeList:
                if i * p > maxNum:
                    break
                isPrime[i * p] = False
                if i % p == 0:
                    mobius[i * p] = 0
                    break
                else:
                    mobius[i * p] = -mobius[i]
                    
        frequency = [0] * (maxNum + 1)
        for num in nums:
            frequency[num] += 1
            
        multiplesCount = [0] * (maxNum + 1)
        for d in range(1, maxNum + 1):
            multiplesCount[d] = sum(frequency[d::d])
            
        nonCoprimeCount = [0] * (maxNum + 1)
        for d in range(2, maxNum + 1):
            if mobius[d] != 0 and multiplesCount[d] != 0:
                val = -mobius[d] * multiplesCount[d]
                for m in range(d, maxNum + 1, d):
                    nonCoprimeCount[m] += val
                    
        maxPossibleScore = -float('inf')
        uniqueNums = set(nums)
        
        for x in range(1, maxNum + 1):
            if x not in uniqueNums and x > maxVal:
                continue
            
            minModificationCost = float('inf')
            
            if x in uniqueNums:
                minModificationCost = min(minModificationCost, max(nonCoprimeCount[x] - 1, 0))
                
            if x <= maxVal:
                minModificationCost = min(minModificationCost, max(nonCoprimeCount[x], 1))
                
            if minModificationCost != float('inf'):
                maxPossibleScore = max(maxPossibleScore, x - minModificationCost)

        return int(maxPossibleScore)