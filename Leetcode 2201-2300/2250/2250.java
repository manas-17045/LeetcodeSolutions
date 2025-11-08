// Leetcode 2250: Count Number of Rectangles Containing Each Point
// https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/
// Solved on 8th of November, 2025
import java.util.*;

class Solution {
    /**
     * Counts the number of rectangles that contain each given point.
     * A rectangle `[li, hi]` contains a point `[xj, yj]` if `li >= xj` and `hi >= yj`.
     * @param rectangles A 2D array where each `rectangles[i] = [li, hi]` represents the length and height of the i-th rectangle.
     * @param points A 2D array where each `points[j] = [xj, yj]` represents the x and y coordinates of the j-th point.
     * @return An array `ans` where `ans[j]` is the number of rectangles that contain the j-th point.
     */
    public int[] countRectangles(int[][] rectangles, int[][] points) {
        int maxH = 100;
        ArrayList<Integer>[] buckets = new ArrayList[maxH + 1];
        for (int i = 0; i <= maxH; i++) buckets[i] = new ArrayList<>();
        for (int[] rect : rectangles) {
            int length = rect[0];
            int height = rect[1];
            if (height >= 0 && height <= maxH) buckets[height].add(length);
        }
        int[][] lensByHeight = new int[maxH + 1][];
        for (int h = 0; h <= maxH; h++) {
            ArrayList<Integer> list = buckets[h];
            Collections.sort(list);
            int sz = list.size();
            int[] arr = new int[sz];
            for (int i = 0; i < sz; i++) arr[i] = list.get(i);
            lensByHeight[h] = arr;
        }
        int m = points.length;
        int[] result = new int[m];
        for (int i = 0; i < m; i++) {
            int x = points[i][0];
            int y = points[i][1];
            int count = 0;
            if (y <= maxH) {
                for (int h = Math.max(0, y); h <= maxH; h++) {
                    int[] arr = lensByHeight[h];
                    if (arr.length == 0) continue;
                    int idx = lowerBound(arr, x);
                    count += arr.length - idx;
                }
            }
            result[i] = count;
        }
        return result;
    }

    private int lowerBound(int[] arr, int target) {
        int l = 0;
        int r = arr.length;
        while (l < r) {
            int mid = (l + r) >>> 1;
            if (arr[mid] < target) l = mid + 1;
            else r = mid;
        }
        return l;
    }
}