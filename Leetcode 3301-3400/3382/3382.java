// Leetcode 3382: Maximum Area Rectangle With Point Constraints II
// https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/
// Solved on 29th of October, 2025
import java.util.Arrays;

class Solution {
    private static class SegmentTree {
        private final int[] tree;
        private final int size;
        private final int initialValue = -1;

        public SegmentTree(int n) {
            size = n;
            tree = new int[4 * n];
            Arrays.fill(tree, initialValue);
        }

        private int merge(int left, int right) {
            return Math.max(left, right);
        }

        private void update(int treeIndex, int lo, int hi, int arrIndex, int val) {
            if (lo == hi) {
                tree[treeIndex] = val;
                return;
            }
            int mid = lo + (hi - lo) / 2;
            if (arrIndex <= mid) {
                update(2 * treeIndex + 1, lo, mid, arrIndex, val);
            } else {
                update(2 * treeIndex + 2, mid + 1, hi, arrIndex, val);
            }
            tree[treeIndex] = merge(tree[2 * treeIndex + 1], tree[2 * treeIndex + 2]);
        }

        public void update(int arrIndex, int val) {
            update(0, 0, size - 1, arrIndex, val);
        }

        private int query(int treeIndex, int lo, int hi, int queryL, int queryR) {
            if (queryL > hi || queryR < lo) {
                return initialValue;
            }
            if (queryL <= lo && hi <= queryR) {
                return tree[treeIndex];
            }
            int mid = lo + (hi - lo) / 2;
            int leftResult = query(2 * treeIndex + 1, lo, mid, queryL, queryR);
            int rightResult = query(2 * treeIndex + 2, mid + 1, hi, queryL, queryR);
            return merge(leftResult, rightResult);
        }

        public int query(int queryL, int queryR) {
            if (queryL > queryR) {
                return initialValue;
            }
            return query(0, 0, size - 1, queryL, queryR);
        }
    }

    /**
     * Calculates the maximum area of a rectangle formed by a subset of given points,
     * such that the rectangle's sides are parallel to the coordinate axes.
     * @param xCoord An array of x-coordinates of the points.
     * @param yCoord An array of y-coordinates of the points.
     * @return The maximum area of such a rectangle, or -1 if no valid rectangle can be formed.
     */
    public long maxRectangleArea(int[] xCoord, int[] yCoord) {
        int n = xCoord.length;
        int[][] points = new int[n][2];
        for (int i = 0; i < n; i++) {
            points[i][0] = xCoord[i];
            points[i][1] = yCoord[i];
        }

        Arrays.sort(points, (a, b) -> {
            if (a[0] != b[0]) {
                return Integer.compare(a[0], b[0]);
            }
            return Integer.compare(a[1], b[1]);
        });

        java.util.Set<Integer> ySet = new java.util.HashSet<>();
        for (int y : yCoord) {
            ySet.add(y);
        }
        java.util.List<Integer> sortedY = new java.util.ArrayList<>(ySet);
        java.util.Collections.sort(sortedY);

        java.util.Map<Integer, Integer> yToIndex = new java.util.HashMap<>();
        for (int i = 0; i < sortedY.size(); i++) {
            yToIndex.put(sortedY.get(i), i);
        }

        long maxArea = -1;
        java.util.Map<Integer, Integer> yToX = new java.util.HashMap<>();
        SegmentTree tree = new SegmentTree(sortedY.size());

        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && points[j][0] == points[i][0]) {
                j++;
            }

            for (int k = i; k < j - 1; k++) {
                int x = points[k][0];
                int y1 = points[k][1];
                int y2 = points[k + 1][1];

                Integer xLeft1 = yToX.get(y1);
                Integer xLeft2 = yToX.get(y2);

                if (xLeft1 != null && xLeft1.equals(xLeft2)) {
                    int xLeft = xLeft1;
                    int yStartIndex = yToIndex.get(y1);
                    int yEndIndex = yToIndex.get(y2);

                    int maxXInside = tree.query(yStartIndex + 1, yEndIndex - 1);

                    if (xLeft > maxXInside) {
                        long width = (long)x - xLeft;
                        long height = (long)y2 - y1;
                        maxArea = Math.max(maxArea, width * height);
                    }
                }
            }

            for (int k = i; k < j; k++) {
                int x = points[k][0];
                int y = points[k][1];
                yToX.put(y, x);
                tree.update(yToIndex.get(y), x);
            }
            i = j;
        }

        return maxArea;
    }
}