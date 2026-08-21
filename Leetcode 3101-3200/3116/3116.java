// Leetcode 3116: Kth Smallest Amount With Single Denomination Combination
// https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/
// Solved on 21st of August, 2026
class Solution {
    /**
     * Finds the k-th smallest amount that can be formed by taking the least common multiple (LCM) of any non-empty subset of the given coins.
     * 
     * @param coins An array of integers representing the coin denominations.
     * @param k The rank of the desired amount (1-indexed).
     * @return The k-th smallest amount.
    */
    public long findKthSmallest(int[] coins, int k) {
        int n = coins.length;
        int subsets = 1 << n;
        long[] lcmArr = new long[subsets];
        int[] signArr = new int[subsets];
        long minCoin = coins[0];

        for (int i = 0; i < n; i++) {
            if (coins[i] < minCoin) {
                minCoin = coins[i];
            }
        }

        for (int i = 1; i < subsets; i++) {
            int lowestBit = i & -i;
            int coinIndex = Integer.numberOfTrailingZeros(lowestBit);
            int prevMask = i ^ lowestBit;

            if (prevMask == 0) {
                lcmArr[i] = coins[cointIndex];
                signArr[i] = 1;
            } else {
                lcmArr[i] = getLcm(lcmArr[prevMask], coins[coinIndex]);
                signArr[i] = signArr[prevMask] * -1;
            }
        }

        long low = 1;
        long high = minCoin * (long) k;
        long ans = high;
        
        while (low <= high) {
            long mid = low + (high - low) / 2;
            long count = 0;
            
            for (int i = 1; i < subsets; i++) {
                count += signArr[i] * (mid / lcmArr[i]);
            }
            
            if (count >= k) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        
        return ans;
    }
    
    private long getLcm(long a, long b) {
        return (a / getGcd(a, b)) * b;
    }
    
    private long getGcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}