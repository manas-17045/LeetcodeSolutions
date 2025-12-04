// Leetcode 2569: Handling Sum Queries After Update
// https://leetcode.com/problems/handling-sum-queries-after-update/
// Solved on 4th of November, 2025
class Solution {
    private int[] tree;
    private boolean[] lazy;

    /**
     * Handles a series of queries on two arrays, nums1 and nums2.
     * @param nums1 The first array, which can be updated.
     * @param nums2 The second array, whose sum is affected by updates to nums1.
     * @param queries A 2D array of queries.
     * @return An array of long representing the results of type 3 queries.
     */
    public long[] handleQuery(int[] nums1, int[] nums2, int[][] queries) {
        int n = nums1.length;
        tree = new int[4 * n];
        lazy = new boolean[4 * n];
        build(nums1, 1, 0, n - 1);

        long sumNums2 = 0;
        for (int num : nums2) {
            sumNums2 += num;
        }

        int resultCount = 0;
        for (int[] query : queries) {
            if (query[0] == 3) {
                resultCount++;
            }
        }

        long[] result = new long[resultCount];
        int resultIndex = 0;

        for (int[] query : queries) {
            int type = query[0];
            if (type == 1) {
                update(1, 0, n - 1, query[1], query[2]);
            } else if (type == 2) {
                sumNums2 += (long) tree[1] * query[1];
            } else if (type == 3) {
                result[resultIndex++] = sumNums2;
            }
        }

        return result;
    }

    private void build(int[] arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = arr[start];
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node, start, mid);
            build(arr, 2 * node + 1, mid + 1, end);
            tree[node] = tree[2 * node] + tree[2 * node + 1];
        }
    }

    private void push(int node, int start, int end) {
        if (lazy[node]) {
            int mid = (start + end) / 2;
            int leftChild = 2 * node;
            int rightChild = 2 * node + 1;

            tree[leftChild] = (mid - start + 1) - tree[leftChild];
            lazy[leftChild] = !lazy[leftChild];

            tree[rightChild] = (end - mid) - tree[rightChild];
            lazy[rightChild] = !lazy[rightChild];

            lazy[node] = false;
        }
    }

    private void update(int node, int start, int end, int l, int r) {
        if (l > end || r < start) {
            return;
        }
        if (l <= start && end <= r) {
            tree[node] = (end - start + 1) - tree[node];
            lazy[node] = !lazy[node];
            return;
        }
        push(node, start, end);
        int mid = (start + end) / 2;
        update(2 * node, start, mid, l, r);
        update(2 * node + 1, mid + 1, end, l, r);
        tree[node] = tree[2 * node] + tree[2 * node + 1];
    }
}