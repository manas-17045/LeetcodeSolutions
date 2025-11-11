// Leetcode 2866: Beautiful Towers II
// https://leetcode.com/problems/beautiful-towers-ii/
// Solved on 11th of November, 2025
import java.util.*;

class Solution {
    /**
     * Calculates the maximum possible sum of heights of a "beautiful tower" configuration.
     * A tower is beautiful if its heights are non-decreasing up to a peak and non-increasing afterwards.
     * @param maxHeights A list of integers representing the maximum allowed height for each tower.
     * @return The maximum sum of heights achievable for a beautiful tower configuration.
     */
    public long maximumSumOfHeights(List<Integer> maxHeights) {
        int n = maxHeights.size();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = maxHeights.get(i);
        }
        long[] left = new long[n];
        long[] right = new long[n];
        Deque<Node> stack = new ArrayDeque<>();
        long curSum = 0;
        for (int i = 0; i < n; i++) {
            int cnt = 1;
            while (!stack.isEmpty() && stack.peek().val > a[i]) {
                Node p = stack.pop();
                cnt += p.count;
                curSum -= (long)p.val * p.count;
            }
            stack.push(new Node(a[i], cnt));
            curSum += (long)a[i] * cnt;
            left[i] = curSum;
        }
        stack.clear();
        curSum = 0;
        for (int i = n - 1; i >= 0; i--) {
            int cnt = 1;
            while (!stack.isEmpty() && stack.peek().val > a[i]) {
                Node p = stack.pop();
                cnt += p.count;
                curSum -= (long)p.val * p.count;
            }
            stack.push(new Node(a[i], cnt));
            curSum += (long)a[i] * cnt;
            right[i] = curSum;
        }
        long best = 0;
        for (int i = 0; i < n; i++) {
            long total = left[i] + right[i] - a[i];
            if (total > best) {
                best = total;
            }
        }
        return best;
    }
    static class Node {
        int val;
        int count;
        Node(int v, int c) {
            val = v;
            count = c;
        }
    }
}