// Leetcode 3245: Alternating Groups III
// https://leetcode.com/problems/alternating-groups-iii/
// Solved on 25th of November, 2025
import java.util.*;

class Solution {
    int n;
    int[] c;
    TreeSet<Integer> bad;
    int[] bitCount;
    int[] bitSum;

    private void update(int[] bit, int idx, int val) {
        for (; idx <= n; idx += idx & -idx) bit[idx] += val;
    }

    private int query(int[] bit, int idx) {
        int sum = 0;
        for (; idx > 0; idx -= idx & -idx) sum += bit[idx];
        return sum;
    }

    private int querySuffix(int[] bit, int k) {
        if (k > n) return 0;
        return query(bit, n) - query(bit, k - 1);
    }

    private int nextBad(int cur) {
        Integer h = bad.higher(cur);
        return h != null ? h : bad.first();
    }

    private void addSegment(int u, int v) {
        int len = (v - u + n) % n;
        if (len == 0) len = n;
        update(bitCount, len, 1);
        update(bitSum, len, len);
    }

    private void removeSegment(int u, int v) {
        int len = (v - u + n) % n;
        if (len == 0) len = n;
        update(bitCount, len, -1);
        update(bitSum, len, -len);
    }

    private void updateBad(int i) {
        if (c[i] == c[(i + 1) % n]) bad.add(i);
        else bad.remove(i);
    }

    /**
     * Calculates the number of alternating groups of a given size after a series of color updates.
     *
     * @param colors An array representing the initial colors of the elements.
     * @param queries A 2D array of queries. Each query is either a type 1 query (get count of alternating groups of a certain size)
     *                or a type 2 query (update the color of an element).
     * @return A list of integers, where each integer is the result of a type 1 query.
     */
    public List<Integer> numberOfAlternatingGroups(int[] colors, int[][] queries) {
        this.c = colors;
        this.n = colors.length;
        this.bad = new TreeSet<>();
        this.bitCount = new int[n + 1];
        this.bitSum = new int[n + 1];

        for (int i = 0; i < n; i++) {
            if (c[i] == c[(i + 1) % n]) bad.add(i);
        }

        if (!bad.isEmpty()) {
            for (int u : bad) {
                addSegment(u, nextBad(u));
            }
        }

        List<Integer> res = new ArrayList<>();

        for (int[] q : queries) {
            if (q[0] == 1) {
                int size = q[1];
                if (bad.isEmpty()) {
                    res.add(size <= n ? n : 0);
                } else {
                    int count = querySuffix(bitCount, size);
                    int sumLen = querySuffix(bitSum, size);
                    res.add(sumLen - (size - 1) * count);
                }
            } else {
                int idx = q[1];
                int col = q[2];
                if (c[idx] == col) continue;

                int prev = (idx - 1 + n) % n;
                Integer pivot = null;
                
                if (!bad.isEmpty()) {
                    for (int x : bad) {
                        if (x != prev && x != idx) {
                            pivot = x;
                            break;
                        }
                    }
                }

                if (pivot == null) {
                    for (int u : bad) removeSegment(u, nextBad(u));
                    c[idx] = col;
                    updateBad(prev);
                    updateBad(idx);
                    for (int u : bad) addSegment(u, nextBad(u));
                } else {
                    int L = prev;
                    while (true) {
                        Integer lower = bad.lower(L);
                        if (lower == null) lower = bad.last();
                        L = lower;
                        if (L != prev && L != idx) break;
                    }

                    int R = idx;
                    while (true) {
                        Integer higher = bad.higher(R);
                        if (higher == null) higher = bad.first();
                        R = higher;
                        if (R != prev && R != idx) break;
                    }

                    int curr = L;
                    while (true) {
                        int nxt = nextBad(curr);
                        removeSegment(curr, nxt);
                        curr = nxt;
                        if (curr == R) break;
                    }

                    c[idx] = col;
                    updateBad(prev);
                    updateBad(idx);

                    curr = L;
                    while (true) {
                        int nxt = nextBad(curr);
                        addSegment(curr, nxt);
                        curr = nxt;
                        if (curr == R) break;
                    }
                }
            }
        }
        return res;
    }
}