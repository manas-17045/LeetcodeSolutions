// Leetcode 3721: Longest Balanced Subarray II
// https://leetcode.com/problems/longest-balanced-subarray-ii/
// Solved on 6th of December, 2025
class Solution {
    private int[] minTree;
    private int[] maxTree;
    private int[] lazyTree;
    private int n;

    /**
     * Finds the length of the longest balanced subarray.
     * A subarray is balanced if the count of even numbers equals the count of odd numbers.
     * @param nums The input array of integers.
     * @return The length of the longest balanced subarray.
     */
    public int longestBalanced(int[] nums) {
        n = nums.length;
        minTree = new int[4 * n];
        maxTree = new int[4 * n];
        lazyTree = new int[4 * n];

        int[] lastPos = new int[100005];
        Arrays.fill(lastPos, -1);

        int maxLen = 0;

        for (int i = 0; i < n; i++) {
            int val = nums[i];
            int change = (val % 2 == 0) ? 1 : -1;
            int prev = lastPos[val];

            update(1, 0, n - 1, prev + 1, i, change);
            lastPos[val] = i;

            int idx = findFirstZero(1, 0, n - 1, 0, i);
            if (idx != -1) {
                maxLen = Math.max(maxLen, i - idx + 1);
            }
        }

        return maxLen;
    }

    private void push(int node) {
        if (lazyTree[node] != 0) {
            lazyTree[2 * node] += lazyTree[node];
            minTree[2 * node] += lazyTree[node];
            maxTree[2 * node] += lazyTree[node];

            lazyTree[2 * node + 1] += lazyTree[node];
            minTree[2 * node + 1] += lazyTree[node];
            maxTree[2 * node + 1] += lazyTree[node];

            lazyTree[node] = 0;
        }
    }

    private void update(int node, int start, int end, int l, int r, int val) {
        if (l > end || r < start) {
            return;
        }

        if (l <= start && end <= r) {
            lazyTree[node] += val;
            minTree[node] += val;
            maxTree[node] += val;
            return;
        }

        push(node);
        int mid = (start + end) / 2;
        update(2 * node, start, mid, l, r, val);
        update(2 * node + 1, mid + 1, end, l, r, val);

        minTree[node] = Math.min(minTree[2 * node], minTree[2 * node + 1]);
        maxTree[node] = Math.max(maxTree[2 * node], maxTree[2 * node + 1]);
    }

    private int findFirstZero(int node, int start, int end, int l, int r) {
        if (l > end || r < start) {
            return -1;
        }

        if (minTree[node] > 0 || maxTree[node] < 0) {
            return -1;
        }

        if (start == end) {
            return (minTree[node] == 0) ? start : -1;
        }

        push(node);
        int mid = (start + end) / 2;

        int res = findFirstZero(2 * node, start, mid, l, r);
        if (res != -1) {
            return res;
        }

        return findFirstZero(2 * node + 1, mid + 1, end, l, r);
    }
}