// Leetcode 3953: Maximum Score with Co-Prime Element
// https://leetcode.com/problems/maximum-score-with-co-prime-element/
// Solved on 22nd of June, 2026
class Solution {
    /**
     * Calculates the maximum score with co-prime element.
     * 
     * @param nums   The array of numbers.
     * @param maxVal The maximum value allowed.
     * @return The maximum score with co-prime element.
     */
    public int maxScore(int[] nums, int maxVal) {
        int maxLimit = 100000;
        int[] spf = new int[maxLimit + 1];
        
        for (int i = 2; i <= maxLimit; i++) {
            spf[i] = i;
        }
        for (int i = 2; i * i <= maxLimit; i++) {
            if (spf[i] == i) {
                for (int j = i * i; j <= maxLimit; j += i) {
                    if (spf[j] == j) {
                        spf[j] = i;
                    }
                }
            }
        }
        
        int[] freq = new int[maxLimit + 1];
        for (int num : nums) {
            freq[num]++;
        }
        
        int[] multiples = new int[maxLimit + 1];
        for (int d = 1; d <= maxLimit; d++) {
            for (int m = d; m <= maxLimit; m += d) {
                multiples[d] += freq[m];
            }
        }
        
        int maxScore = Integer.MIN_VALUE;
        int[] primes = new int[10];
        
        for (int x = 1; x <= maxLimit; x++) {
            boolean isValidCandidate = (x <= maxVal) || (freq[x] > 0);
            if (!isValidCandidate) {
                continue;
            }
            
            if (x == 1) {
                int cost = (freq[1] > 0) ? 0 : 1;
                if (1 - cost > maxScore) {
                    maxScore = 1 - cost;
                }
                continue;
            }
            
            int temp = x;
            int primeCount = 0;
            while (temp > 1) {
                int p = spf[temp];
                primes[primeCount++] = p;
                while (temp % p == 0) {
                    temp /= p;
                }
            }
            
            int nonCoprimeCount = 0;
            int totalSubsets = 1 << primeCount;
            
            for (int mask = 1; mask < totalSubsets; mask++) {
                int product = 1;
                int setBits = 0;
                for (int i = 0; i < primeCount; i++) {
                    if ((mask & (1 << i)) != 0) {
                        product *= primes[i];
                        setBits++;
                    }
                }
                if ((setBits & 1) == 1) {
                    nonCoprimeCount += multiples[product];
                } else {
                    nonCoprimeCount -= multiples[product];
                }
            }
            
            int minCost = Integer.MAX_VALUE;
            
            if (freq[x] > 0) {
                if (nonCoprimeCount - 1 < minCost) {
                    minCost = nonCoprimeCount - 1;
                }
            }
            
            if (x <= maxVal) {
                if (nonCoprimeCount > 0) {
                    if (nonCoprimeCount < minCost) {
                        minCost = nonCoprimeCount;
                    }
                } else {
                    if (1 < minCost) {
                        minCost = 1;
                    }
                }
            }
            
            if (minCost != Integer.MAX_VALUE) {
                if (x - minCost > maxScore) {
                    maxScore = x - minCost;
                }
            }
        }
        
        return maxScore;
    }
}