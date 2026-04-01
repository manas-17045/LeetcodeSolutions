// Leetcode 3569: Maximize Count of Distinct Primes After Split
// https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/
// Solved on 1st of April, 2026
import java.util.TreeSet;

class Solution {
    class SegmentTree {
        int[] tree;
        int[] lazy;

        public SegmentTree(int size) {
            tree = new int[4 * size + 1];
            lazy = new int[4 * size + 1];
        }

        public void update(int node, int start, int end, int l, int r, int val) {
            if (lazy[node] != 0) {
                tree[node] += lazy[node];
                if (start != end) {
                    lazy[2 * node] += lazy[node];
                    lazy[2 * node + 1] += lazy[node];
                }
                lazy[node] = 0;
            }
            if (start > end || start > r || end < l) {
                return;
            }
            if (start >= l && end <= r) {
                tree[node] += val;
                if (start != end) {
                    lazy[2 * node] += val;
                    lazy[2 * node + 1] += val;
                }
                return;
            }
            int mid = start + (end - start) / 2;
            update(2 * node, start, mid, l, r, val);
            update(2 * node + 1, mid + 1, end, l, r, val);
            tree[node] = Math.max(tree[2 * node], tree[2 * node + 1]);
        }

        public int query(int node, int start, int end, int l, int r) {
            if (lazy[node] != 0) {
                tree[node] += lazy[node];
                if (start != end) {
                    lazy[2 * node] += lazy[node];
                    lazy[2 * node + 1] += lazy[node];
                }
                lazy[node] = 0;
            }
            if (start > end || start > r || end < l) {
                return 0;
            }
            if (start >= l && end <= r) {
                return tree[node];
            }
            int mid = start + (end - start) / 2;
            int leftMax = query(2 * node, start, mid, l, r);
            int rightMax = query(2 * node + 1, mid + 1, end, l, r);
            return Math.max(leftMax, rightMax);
        }
    }

    /**
     * Calculates the maximum number of distinct primes after splitting the array at any index.
     *
     * @param nums    The initial array of integers.
     * @param queries A 2D array where each query is [index, newValue] to update nums.
     * @return        An array containing the maximum distinct prime count for each query.
     */
    public int[] maximumCount(int[] nums, int[][] queries) {
        int n = nums.length;
        int maxVal = 100000;
        boolean[] isPrime = new boolean[maxVal + 1];
        
        for (int i = 2; i <= maxVal; i++) {
            isPrime[i] = true;
        }
        for (int i = 2; i * i <= maxVal; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= maxVal; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        TreeSet<Integer>[] pos = new TreeSet[maxVal + 1];
        for (int i = 0; i <= maxVal; i++) {
            if (isPrime[i]) {
                pos[i] = new TreeSet<>();
            }
        }

        SegmentTree segTree = new SegmentTree(n);
        int totalPrimes = 0;

        for (int i = 0; i < n; i++) {
            int val = nums[i];
            if (isPrime[val]) {
                if (pos[val].isEmpty()) {
                    totalPrimes++;
                } else {
                    int first = pos[val].first();
                    int last = pos[val].last();
                    if (first + 1 <= last) {
                        segTree.update(1, 1, n - 1, first + 1, last, -1);
                    }
                }
                pos[val].add(i);
                int first = pos[val].first();
                int last = pos[val].last();
                if (first + 1 <= last) {
                    segTree.update(1, 1, n - 1, first + 1, last, 1);
                }
            }
        }

        int q = queries.length;
        int[] ans = new int[q];

        for (int i = 0; i < q; i++) {
            int idx = queries[i][0];
            int newVal = queries[i][1];
            int oldVal = nums[idx];

            if (oldVal != newVal) {
                if (isPrime[oldVal]) {
                    int first = pos[oldVal].first();
                    int last = pos[oldVal].last();
                    if (first + 1 <= last) {
                        segTree.update(1, 1, n - 1, first + 1, last, -1);
                    }
                    pos[oldVal].remove(idx);
                    if (pos[oldVal].isEmpty()) {
                        totalPrimes--;
                    } else {
                        first = pos[oldVal].first();
                        last = pos[oldVal].last();
                        if (first + 1 <= last) {
                            segTree.update(1, 1, n - 1, first + 1, last, 1);
                        }
                    }
                }

                if (isPrime[newVal]) {
                    if (pos[newVal].isEmpty()) {
                        totalPrimes++;
                    } else {
                        int first = pos[newVal].first();
                        int last = pos[newVal].last();
                        if (first + 1 <= last) {
                            segTree.update(1, 1, n - 1, first + 1, last, -1);
                        }
                    }
                    pos[newVal].add(idx);
                    int first = pos[newVal].first();
                    int last = pos[newVal].last();
                    if (first + 1 <= last) {
                        segTree.update(1, 1, n - 1, first + 1, last, 1);
                    }
                }
                nums[idx] = newVal;
            }

            int maxOverlap = segTree.query(1, 1, n - 1, 1, n - 1);
            ans[i] = totalPrimes + maxOverlap;
        }

        return ans;
    }
}