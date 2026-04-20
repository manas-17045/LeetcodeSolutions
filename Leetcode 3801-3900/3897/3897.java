// Leetcode 3897: Maximum Value of Concatenated Binary Segments
// https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments/
// Solved on 20th of April, 2026
class Solution {
    /**
     * Calculates the maximum value of concatenated binary segments formed by pairs of 1s and 0s.
     *
     * @param nums1 An array where nums1[i] represents the number of set bits (1s) in the i-th segment.
     * @param nums0 An array where nums0[i] represents the number of unset bits (0s) in the i-th segment.
     * @return The maximum possible value of the concatenated binary string modulo 10^9 + 7.
     */
    public int maxValue(int[] nums1, int[] nums0) {
        int n = nums1.length;
        Integer[] indices = new Integer[n];
        int totalLen = 0;
        
        for (int i = 0; i < n; i++) {
            indices[i] = i;
            totalLen += nums1[i] + nums0[i];
        }
        
        Arrays.sort(indices, (a, b) -> {
            int o1 = nums1[a];
            int z1 = nums0[a];
            int o2 = nums1[b];
            int z2 = nums0[b];
            
            int l1 = z1 == 0 ? o1 + o2 : o1;
            int l2 = z2 == 0 ? o2 + o1 : o2;
            
            if (l1 != l2) {
                return l2 < l1 ? -1 : 1;
            }
            
            int nz1 = z1 == 0 ? z2 : z1;
            int nz2 = z2 == 0 ? z1 : z2;
            
            if (nz1 != nz2) {
                return nz1 < nz2 ? -1 : 1;
            }
            
            return 0;
        });
        
        int mod = 1000000007;
        int[] p = new int[totalLen + 1];
        p[0] = 1;
        
        for (int i = 1; i <= totalLen; i++) {
            p[i] = (int) (((long) p[i - 1] * 2) % mod);
        }
        
        long ans = 0;
        
        for (int i = 0; i < n; i++) {
            int idx = indices[i];
            int o = nums1[idx];
            int z = nums0[idx];
            
            long val = (long) (p[o] - 1) * p[z] % mod;
            ans = (ans * p[o + z] + val) % mod;
        }
        
        return (int) ans;
    }
}