// Leetcode 3296: Minimum Number of Seconds to Make Mountain Height Zero
// https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/
// Solved on 13th of March, 2026
class Solution {
    /**
     * Calculates the minimum number of seconds required to reduce the mountain height to zero.
     * 
     * @param mountainHeight The initial height of the mountain.
     * @param workerTimes An array where workerTimes[i] is the base time for the i-th worker.
     * @return The minimum number of seconds needed for all workers to reduce the height to zero.
     */
    public long minNumberOfSeconds(int mountainHeight, int[] workerTimes) {
        int minWorkerTime = workerTimes[0];
        for (int time : workerTimes) {
            if (time < minWorkerTime) {
                minWorkerTime = time;
            }
        }
        
        long left = 1;
        long right = (long) minWorkerTime * mountainHeight * (mountainHeight + 1) / 2;
        long minimumSeconds = right;
        
        while (left <= right) {
            long mid = left + (right - left) / 2;
            long totalReducedHeight = 0;
            
            for (int time : workerTimes) {
                long lowHeight = 0;
                long highHeight = mountainHeight;
                long workerMaxReduced = 0;
                
                while (lowHeight <= highHeight) {
                    long currentHeight = lowHeight + (highHeight - lowHeight) / 2;
                    if ((long) time * currentHeight * (currentHeight + 1) / 2 <= mid) {
                        workerMaxReduced = currentHeight;
                        lowHeight = currentHeight + 1;
                    } else {
                        highHeight = currentHeight - 1;
                    }
                }
                totalReducedHeight += workerMaxReduced;
            }
            
            if (totalReducedHeight >= mountainHeight) {
                minimumSeconds = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        
        return minimumSeconds;
    }
}