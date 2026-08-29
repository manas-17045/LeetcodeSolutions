# Leetcode 4007: Widest Possible Fence
# https://leetcode.com/problems/widest-possible-fence/
# Solved on 29th of August, 2026
class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        """
        Calculates the maximum possible width of a fence where all planks have the same height.
        
        Args:
            planks (list[int]): A list of integers representing the heights of the wooden planks.
            
        Returns:
            int: The maximum possible width of the fence that can be built.
        """
        freqMap = {}
        for plankHeight in planks:
            freqMap[plankHeight] = freqMap.get(plankHeight, 0) + 1

        uniqueHeights = list(freqMap.keys())
        pairContributions = {}

        for i in range(len(uniqueHeights)):
            firstPlank = uniqueHeights[i]
            doubleHeight = firstPlank + firstPlank
            pairContributions[doubleHeight] = pairContributions.get(doubleHeight, 0) + (freqMap[firstPlank] // 2)

            for j in range(i + 1, len(uniqueHeights)):
                secondPlank = uniqueHeights[j]
                targetHeight = firstPlank + secondPlank
                possiblePairs = min(freqMap[firstPlank], freqMap[secondPlank])
                pairContributions[targetHeight] = pairContributions.get(targetHeight, 0) + possiblePairs

        maxWidth = 0
        allPossibleHeights = set(freqMap.keys()) | set(pairContributions.keys())

        for height in allPossibleHeights:
            currentWidth = freqMap.get(height, 0) + pairContributions.get(height, 0)
            if currentWidth > maxWidth:
                maxWidth = currentWidth

        return maxWidth