// Leetcode 2234: Maximum Total Beauty of the Gardens
// https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/
// Solved on 27th of October, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the maximum total beauty of the gardens.
     * @param flowers An array of integers representing the initial number of flowers in each garden.
     * @param newFlowers The total number of new flowers available to plant.
     * @param target The target number of flowers for a garden to be considered full.
     * @param full The beauty score for each full garden.
     * @param partial The beauty score for each flower in a partially filled garden.
     * @return The maximum total beauty that can be achieved.
     */
    public long maximumBeauty(int[] flowers, long newFlowers, int target, int full, int partial) {
        int n = flowers.length;
        long[] gardens = new long[n];
        for (int i = 0; i < n; i++) {
            gardens[i] = flowers[i];
        }
        Arrays.sort(gardens);

        long[] costPrefixSum = new long[n + 1];
        costPrefixSum[0] = 0;
        for (int i = 0; i < n; i++) {
            costPrefixSum[i + 1] = costPrefixSum[i] + gardens[i];
        }

        long maxBeauty = 0;
        
        int j = lowerBound(gardens, n, target);
        int numAlreadyFull = n - j;
        
        long costToMakeFull = 0;

        for (int keptIncomplete = j; keptIncomplete >= 0; keptIncomplete--) {
            long flowersLeft = newFlowers - costToMakeFull;
            if (flowersLeft < 0) {
                break;
            }

            long minPartial = 0;
            if (keptIncomplete > 0) {
                long low = 0;
                long high = target - 1;
                long bestPartial = 0;

                while (low <= high) {
                    long level = low + (high - low) / 2;
                    if (isPossible(level, keptIncomplete, flowersLeft, gardens, costPrefixSum)) {
                        bestPartial = level;
                        low = level + 1;
                    } else {
                        high = level - 1;
                    }
                }
                minPartial = bestPartial;
            }

            long numFull = numAlreadyFull + (j - keptIncomplete);
            long currentBeauty = numFull * full + minPartial * partial;
            maxBeauty = Math.max(maxBeauty, currentBeauty);

            if (keptIncomplete > 0) {
                costToMakeFull += (target - gardens[keptIncomplete - 1]);
            }
        }

        return maxBeauty;
    }

    private boolean isPossible(long level, int count, long flowersLeft, long[] gardens, long[] costPrefixSum) {
        int index = lowerBound(gardens, count, level);
        long cost = (long)index * level - costPrefixSum[index];
        return cost <= flowersLeft;
    }

    private int lowerBound(long[] arr, int end, long target) {
        int low = 0;
        int high = end;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] >= target) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
}