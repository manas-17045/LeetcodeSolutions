// Leetcode 3901: Good Subsequence Queries
// https://leetcode.com/problems/good-subsequence-queries/
// Solved on 27th of April, 2026
class Solution {
    static int[][] primeFactors;
    
    static {
        int maxVal = 50000;
        primeFactors = new int[maxVal + 1][];
        int[] count = new int[maxVal + 1];
        int[][] temp = new int[maxVal + 1][7];
        
        for (int i = 2; i <= maxVal; i++) {
            if (count[i] == 0) {
                for (int j = i; j <= maxVal; j += i) {
                    temp[j][count[j]++] = i;
                }
            }
        }
        
        for (int i = 2; i <= maxVal; i++) {
            primeFactors[i] = new int[count[i]];
            for (int j = 0; j < count[i]; j++) {
                primeFactors[i][j] = temp[i][j];
            }
        }
        primeFactors[1] = new int[0];
    }

    /**
     * Counts the number of queries that result in a "good" subsequence configuration.
     *
     * @param nums    An array of integers.
     * @param p       A prime number used as a divisor for the subsequence condition.
     * @param queries A 2D array where each query is [index, newValue] to update nums.
     * @return The total count of queries after which the condition is met.
     */
    public int countGoodSubseq(int[] nums, int p, int[][] queries) {
        int n = nums.length;
        int[] freq = new int[50005];
        int[] countOfFreq = new int[n + 1];
        int countP = 0;

        for (int i = 0; i < n; i++) {
            if (nums[i] % p == 0) {
                countP++;
                int reduced = nums[i] / p;
                for (int q : primeFactors[reduced]) {
                    if (freq[q] > 0) {
                        countOfFreq[freq[q]]--;
                    }
                    freq[q]++;
                    countOfFreq[freq[q]]++;
                }
            }
        }

        int ans = 0;

        for (int k = 0; k < queries.length; k++) {
            int ind = queries[k][0];
            int val = queries[k][1];
            int oldVal = nums[ind];

            if (oldVal % p == 0) {
                int reduced = oldVal / p;
                for (int q : primeFactors[reduced]) {
                    countOfFreq[freq[q]]--;
                    freq[q]--;
                    if (freq[q] > 0) {
                        countOfFreq[freq[q]]++;
                    }
                }
                countP--;
            }

            nums[ind] = val;

            if (val % p == 0) {
                countP++;
                int reduced = val / p;
                for (int q : primeFactors[reduced]) {
                    if (freq[q] > 0) {
                        countOfFreq[freq[q]]--;
                    }
                    freq[q]++;
                    countOfFreq[freq[q]]++;
                }
            }

            if (countP > 0) {
                if (countOfFreq[countP] == 0) {
                    if (countP < n) {
                        ans++;
                    } else {
                        if (n > 6) {
                            ans++;
                        } else {
                            boolean possible = false;
                            for (int i = 0; i < n; i++) {
                                int g = 0;
                                for (int j = 0; j < n; j++) {
                                    if (i != j) {
                                        g = getGcd(g, nums[j] / p);
                                    }
                                }
                                if (g == 1) {
                                    possible = true;
                                    break;
                                }
                            }
                            if (possible) {
                                ans++;
                            }
                        }
                    }
                }
            }
        }

        return ans;
    }

    private int getGcd(int a, int b) {
        while (b != 0) {
            int t = b;
            b = a % b;
            a = t;
        }
        return a;
    }
}