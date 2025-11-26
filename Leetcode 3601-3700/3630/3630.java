// Leetcode 3630: Partition Array for Maximum XOR and AND
// https://leetcode.com/problems/partition-array-for-maximum-xor-and-and/
// Solved on 26th of November, 2025
class Solution {
    private long maxVal;
    private int[] basis = new int[30];
    
    /**
     * Maximizes the expression `xorM + (maxX * 2) + andB` by partitioning the input array `nums`.
     * The partitioning involves selecting a subsequence for `xorM` and `andB`, and the remaining elements
     * are used to maximize `maxX` through a XOR basis.
     *
     * @param nums The input array of integers.
     * @return The maximum possible value of the expression.
     */
    public long maximizeXorAndXor(int[] nums) {
        maxVal = 0;
        dfs(nums, 0, 0, 0, true);
        return maxVal;
    }

    private void dfs(int[] nums, int idx, int xorM, int andB, boolean bEmpty) {
        if (idx == nums.length) {
            int[] tempBasis = new int[30];
            for (int b : basis) {
                if (b != 0) {
                    insert(tempBasis, b & ~xorM);
                }
            }
            
            long maxX = 0;
            for (int i = 29; i >= 0; i--) {
                if (tempBasis[i] == 0) continue;
                if ((maxX ^ tempBasis[i]) > maxX) {
                    maxX ^= tempBasis[i];
                }
            }
            
            long term1 = xorM + (maxX * 2);
            long term2 = bEmpty ? 0 : andB;
            maxVal = Math.max(maxVal, term1 + term2);
            return;
        }

        int val = nums[idx];

        dfs(nums, idx + 1, xorM, bEmpty ? val : (andB & val), false);

        int recordedIdx = -1;
        int temp = val;
        for (int i = 29; i >= 0; i--) {
            if ((temp & (1 << i)) != 0) {
                if (basis[i] == 0) {
                    basis[i] = temp;
                    recordedIdx = i;
                    break;
                }
                temp ^= basis[i];
            }
        }

        dfs(nums, idx + 1, xorM ^ val, andB, bEmpty);

        if (recordedIdx != -1) {
            basis[recordedIdx] = 0;
        }
    }

    private void insert(int[] bArr, int val) {
        for (int i = 29; i >= 0; i--) {
            if ((val & (1 << i)) != 0) {
                if (bArr[i] == 0) {
                    bArr[i] = val;
                    return;
                }
                val ^= bArr[i];
            }
        }
    }
}