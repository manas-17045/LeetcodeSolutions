// Leetcode 2213: Longest Substring of one Repeating Character
// https://leetcode.com/problems/longest-substring-of-one-repeating-character/ 
// Solved on 13th of August, 2026
class Solution {
    int[] maxLen;
    int[] preLen;
    int[] sufLen;

    /**
     * Computes the longest substring of repeating characters after each query.
     * 
     * @param s The initial string.
     * @param queryCharacters The characters to update in the string.
     * @param queryIndices The indices to update in the string.
     * @return An array of integers representing the length of the longest substring of repeating characters after each query.
     */
    public int longestRepeating(String s, String queryCharacters, int[] queryIndices) {
        int n = s.length();
        int k = queryCharacters.length();
        maxLen = new int[4 * n];
        preLen = new int[4 * n];
        sufLen = new int[4 * n];
        char[] arr = s.toCharArray();
        
        build(0, 0, n - 1, arr);
        
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            int idx = queryIndices[i];
            arr[idx] = queryCharacters.charAt(i);
            update(0, 0, n - 1, idx, arr);
            result[i] = maxLen[0];
        }
        
        return result;
    }

    private void build(int node, int start, int end, char[] arr) {
        if (start == end) {
            maxLen[node] = 1;
            preLen[node] = 1;
            sufLen[node] = 1;
            return;
        }
        int mid = start + (end - start) / 2;
        int left = 2 * node + 1;
        int right = 2 * node + 2;
        build(left, start, mid, arr);
        build(right, mid + 1, end, arr);
        merge(node, left, right, start, mid, end, arr);
    }

    private void update(int node, int start, int end, int idx, char[] arr) {
        if (start == end) {
            return;
        }
        int mid = start + (end - start) / 2;
        int left = 2 * node + 1;
        int right = 2 * node + 2;
        if (idx <= mid) {
            update(left, start, mid, idx, arr);
        } else {
            update(right, mid + 1, end, idx, arr);
        }
        merge(node, left, right, start, mid, end, arr);
    }

    private void merge(int node, int left, int right, int start, int mid, int end, char[] arr) {
        int leftSize = mid - start + 1;
        int rightSize = end - mid;
        
        maxLen[node] = Math.max(maxLen[left], maxLen[right]);
        preLen[node] = preLen[left];
        sufLen[node] = sufLen[right];
        
        if (arr[mid] == arr[mid + 1]) {
            maxLen[node] = Math.max(maxLen[node], sufLen[left] + preLen[right]);
            if (preLen[left] == leftSize) {
                preLen[node] += preLen[right];
            }
            if (sufLen[right] == rightSize) {
                sufLen[node] += sufLen[left];
            }
        }
    }
}