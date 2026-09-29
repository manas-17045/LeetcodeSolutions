// Leetcode 4037: Maximum Valid Split Positions II
// https://leetcode.com/problems/maximum-valid-split-positions-ii/
// Solved on 29th of September, 2026
class Solution {
    /**
     * Calculates the maximum possible score of the array after removing at most one element.
     * The score is determined by the number of valid split positions where the greatest
     * common divisor (GCD) of the left part equals the GCD of the right part.
     * 
     * @param nums the input array of integers
     * @return the maximum possible score after at most one element removal
     */
    public int maxValidSplits(int[] nums) {
        int n = nums.length;
        int[] pref = new int[n];
        pref[0] = nums[0];
        
        for (int i = 1; i < n; i++) {
            pref[i] = gcd(pref[i - 1], nums[i]);
        }
        
        int[] suff = new int[n];
        suff[n - 1] = nums[n - 1];
        
        for (int i = n - 2; i >= 0; i--) {
            suff[i] = gcd(suff[i + 1], nums[i]);
        }
        
        boolean[] isCandidate = new boolean[n];
        isCandidate[0] = true;
        isCandidate[n - 1] = true;
        
        for (int i = 1; i < n; i++) {
            if (pref[i] != pref[i - 1]) {
                isCandidate[i] = true;
            }
        }
        
        for (int i = 0; i < n - 1; i++) {
            if (suff[i] != suff[i + 1]) {
                isCandidate[i] = true;
            }
        }
        
        int maxScore = 0;
        
        for (int i = 0; i < n - 1; i++) {
            if (pref[i] == suff[i + 1]) {
                maxScore++;
            }
        }
        
        int[] prefixGcd = new int[n - 1];
        int[] suffixGcd = new int[n - 1];
        
        for (int c = 0; c < n; c++) {
            if (!isCandidate[c]) {
                continue;
            }
            
            int currentPref = 0;
            int prefIndex = 0;
            
            for (int i = 0; i < n; i++) {
                if (i == c) {
                    continue;
                }
                currentPref = gcd(currentPref, nums[i]);
                prefixGcd[prefIndex++] = currentPref;
            }
            
            int currentSuff = 0;
            int suffIndex = n - 2;
            
            for (int i = n - 1; i >= 0; i--) {
                if (i == c) {
                    continue;
                }
                currentSuff = gcd(currentSuff, nums[i]);
                suffixGcd[suffIndex--] = currentSuff;
            }
            
            int score = 0;
            
            for (int i = 0; i < n - 2; i++) {
                if (prefixGcd[i] == suffixGcd[i + 1]) {
                    score++;
                }
            }
            
            if (score > maxScore) {
                maxScore = score;
            }
        }
        
        return maxScore;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}