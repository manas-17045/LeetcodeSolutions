// Leetcode 4007: Widest Possible Fence
// https://leetcode.com/problems/widest-possible-fence/
// Solved on the 29th of August, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the maximum possible width of a fence that can be built
     * using wooden planks of the same height. Planks can be used as is,
     * or combined by summing the heights of exactly two distinct original planks.
     *
     * @param planks an array of integers representing the heights of the wooden planks
     * @return the maximum possible width of the fence
     */
    public int maximumWidth(int[] planks) {
        Arrays.sort(planks);
        
        int totalPlanks = planks.length;
        int[] uniqueHeights = new int[totalPlanks];
        int[] heightFrequencies = new int[totalPlanks];
        int distinctCount = 0;
        
        for (int i = 0; i < totalPlanks; i++) {
            if (i == 0 || planks[i] != planks[i - 1]) {
                uniqueHeights[distinctCount] = planks[i];
                heightFrequencies[distinctCount] = 1;
                distinctCount++;
            } else {
                heightFrequencies[distinctCount - 1]++;
            }
        }
        
        int maxFenceWidth = 0;
        for (int i = 0; i < distinctCount; i++) {
            maxFenceWidth = Math.max(maxFenceWidth, heightFrequencies[i]);
        }
        
        int maximumPossiblePairs = distinctCount * (distinctCount + 1) / 2;
        long[] sumConfigurations = new long[maximumPossiblePairs];
        int configurationCount = 0;
        
        for (int i = 0; i < distinctCount; i++) {
            for (int j = i; j < distinctCount; j++) {
                int combinedHeight = uniqueHeights[i] + uniqueHeights[j];
                int pairCount = (i == j) ? (heightFrequencies[i] / 2) : Math.min(heightFrequencies[i], heightFrequencies[j]);
                
                if (pairCount > 0) {
                    sumConfigurations[configurationCount++] = ((long) combinedHeight << 32) | pairCount;
                }
            }
        }
        
        Arrays.sort(sumConfigurations, 0, configurationCount);
        
        int currentCombinedHeight = -1;
        int currentTotalPairs = 0;
        
        for (int i = 0; i < configurationCount; i++) {
            long currentConfiguration = sumConfigurations[i];
            int combinedHeight = (int) (currentConfiguration >>> 32);
            int pairCount = (int) (currentConfiguration & 0xFFFFFFFFL);
            
            if (combinedHeight != currentCombinedHeight) {
                if (currentCombinedHeight != -1) {
                    int singlePlankCount = getFrequency(uniqueHeights, heightFrequencies, distinctCount, currentCombinedHeight);
                    maxFenceWidth = Math.max(maxFenceWidth, currentTotalPairs + singlePlankCount);
                }
                currentCombinedHeight = combinedHeight;
                currentTotalPairs = pairCount;
            } else {
                currentTotalPairs += pairCount;
            }
        }
        
        if (currentCombinedHeight != -1) {
            int singlePlankCount = getFrequency(uniqueHeights, heightFrequencies, distinctCount, currentCombinedHeight);
            maxFenceWidth = Math.max(maxFenceWidth, currentTotalPairs + singlePlankCount);
        }
        
        return maxFenceWidth;
    }

    private int getFrequency(int[] uniqueHeights, int[] heightFrequencies, int distinctCount, int targetHeight) {
        int leftIndex = 0;
        int rightIndex = distinctCount - 1;
        
        while (leftIndex <= rightIndex) {
            int midIndex = leftIndex + (rightIndex - leftIndex) / 2;
            if (uniqueHeights[midIndex] == targetHeight) {
                return heightFrequencies[midIndex];
            }
            if (uniqueHeights[midIndex] < targetHeight) {
                leftIndex = midIndex + 1;
            } else {
                rightIndex = midIndex - 1;
            }
        }
        
        return 0;
    }
}