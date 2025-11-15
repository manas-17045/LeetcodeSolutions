// Leetcode 1850: Minimum Adjacent Swaps to Reach the Kth Smallest Number
// https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/
// Solved on 15th of November, 2025
class Solution {
    /**
     * Calculates the minimum number of adjacent swaps required to transform the original number string
     * into its k-th smallest permutation.
     * @param num The original number string.
     * @param k The k-th smallest permutation to reach.
     * @return The minimum number of adjacent swaps.
     */
    public int getMinSwaps(String num, int k) {
        char[] target = num.toCharArray();
        for (int i = 0; i < k; i++) {
            nextPermutation(target);
        }
        char[] source = num.toCharArray();
        int n = source.length;
        int swaps = 0;
        for (int i = 0; i < n; i++) {
            if (source[i] == target[i]) continue;
            int j = i + 1;
            while (j < n && source[j] != target[i]) j++;
            while (j > i) {
                char tmp = source[j];
                source[j] = source[j - 1];
                source[j - 1] = tmp;
                j--;
                swaps++;
            }
        }
        return swaps;
    }

    private void nextPermutation(char[] a) {
        int n = a.length;
        int i = n - 2;
        while (i >= 0 && a[i] >= a[i + 1]) i--;
        if (i >= 0) {
            int j = n - 1;
            while (a[j] <= a[i]) j--;
            char tmp = a[i];
            a[i] = a[j];
            a[j] = tmp;
        }
        reverse(a, i + 1, n - 1);
    }

    private void reverse(char[] a, int l, int r) {
        while (l < r) {
            char tmp = a[l];
            a[l] = a[r];
            a[r] = tmp;
            l++;
            r--;
        }
    }
}