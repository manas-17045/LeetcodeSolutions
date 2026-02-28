// Leetcode 3501: Maximize Active Section with Trade II
// https://leetcode.com/problems/maximize-active-section-with-trade-ii/
// Solved on 28th of February, 2026
import java.util.ArrayList;
import java.util.List;

class Solution {
    class SegTree {
        int[] tree;
        int[] arr;
        int n;

        public SegTree(int[] arr) {
            this.arr = arr;
            this.n = arr.length;
            if (n > 0) {
                tree = new int[4 * n];
                build(1, 0, n - 1);
            }
        }

        private void build(int node, int start, int end) {
            if (start == end) {
                tree[node] = arr[start];
            } else {
                int mid = start + (end - start) / 2;
                build(2 * node, start, mid);
                build(2 * node + 1, mid + 1, end);
                tree[node] = Math.max(tree[2 * node], tree[2 * node + 1]);
            }
        }

        public int query(int ql, int qr) {
            if (n == 0 || ql > qr) {
                return 0;
            }
            return query(1, 0, n - 1, ql, qr);
        }

        private int query(int node, int start, int end, int ql, int qr) {
            if (qr < start || ql > end) {
                return 0;
            }
            if (ql <= start && end <= qr) {
                return tree[node];
            }
            int mid = start + (end - start) / 2;
            int p1 = query(2 * node, start, mid, ql, qr);
            int p2 = query(2 * node + 1, mid + 1, end, ql, qr);
            return Math.max(p1, p2);
        }
    }

    /**
     * Calculates the maximum number of active sections (ones) after performing a trade 
     * within the specified query ranges.
     * 
     * @param s The initial binary string.
     * @param queries A 2D array where each query is [l, r] representing the trade range.
     * @return A list of integers representing the maximum active sections for each query.
     */
    public List<Integer> maxActiveSectionsAfterTrade(String s, int[][] queries) {
        int totalOnes = 0;
        int n = s.length();
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '1') {
                totalOnes++;
            }
        }

        List<Integer> startsList = new ArrayList<>();
        List<Integer> endsList = new ArrayList<>();

        int i = 0;
        while (i < n) {
            if (s.charAt(i) == '0') {
                int startIdx = i;
                while (i < n && s.charAt(i) == '0') {
                    i++;
                }
                startsList.add(startIdx);
                endsList.add(i - 1);
            } else {
                i++;
            }
        }

        int m = startsList.size();
        int[] starts = new int[m];
        int[] ends = new int[m];
        for (int j = 0; j < m; j++) {
            starts[j] = startsList.get(j);
            ends[j] = endsList.get(j);
        }

        int[] w = new int[Math.max(0, m - 1)];
        for (int j = 0; j < m - 1; j++) {
            w[j] = (ends[j] - starts[j] + 1) + (ends[j + 1] - starts[j + 1] + 1);
        }

        SegTree segTree = new SegTree(w);
        List<Integer> result = new ArrayList<>();

        for (int[] q : queries) {
            int l = q[0];
            int r = q[1];

            int x = findX(ends, l);
            int y = findY(starts, r);

            if (x > y || x == m || y == -1) {
                result.add(totalOnes);
            } else if (x == y) {
                result.add(totalOnes);
            } else if (y == x + 1) {
                int len1 = Math.min(r, ends[x]) - Math.max(l, starts[x]) + 1;
                int len2 = Math.min(r, ends[y]) - Math.max(l, starts[y]) + 1;
                result.add(totalOnes + len1 + len2);
            } else {
                int len1 = Math.min(r, ends[x]) - Math.max(l, starts[x]) + 1;
                len1 += (ends[x + 1] - starts[x + 1] + 1);

                int len2 = (ends[y - 1] - starts[y - 1] + 1);
                len2 += Math.min(r, ends[y]) - Math.max(l, starts[y]) + 1;

                int len3 = segTree.query(x + 1, y - 2);

                int maxIncrease = Math.max(len1, Math.max(len2, len3));
                result.add(totalOnes + maxIncrease);
            }
        }

        return result;
    }

    private int findX(int[] ends, int l) {
        int low = 0;
        int high = ends.length - 1;
        int ans = ends.length;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (ends[mid] >= l) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }

    private int findY(int[] starts, int r) {
        int low = 0;
        int high = starts.length - 1;
        int ans = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (starts[mid] <= r) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }
}