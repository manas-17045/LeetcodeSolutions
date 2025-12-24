// Leetcode 3777: Minimum Deletions to Make Alternating Substring
// https://leetcode.com/problems/minimum-deletions-to-make-alternating-substring/
// Solved on 24th of December, 2025
import java.util.Arrays;

class Solution {
    private int[] tree;
    private int n;

    private void update(int index, int val) {
        index++;
        while (index <= n) {
            tree[index] += val;
            index += index & (-index);
        }
    }

    private int query(int index) {
        index++;
        int sum = 0;
        while (index > 0) {
            sum += tree[index];
            index -= index & (-index);
        }
        return sum;
    }

    /**
     * Calculates the minimum deletions to make an alternating substring based on a series of queries.
     * @param s The initial string.
     * @param queries An array of queries. Each query is either a type 1 (update character) or type 2 (count deletions in a range).
     * @return An array of integers, where each element is the result of a type 2 query.
     */
    public int[] minDeletions(String s, int[][] queries) {
        n = s.length();
        tree = new int[n + 1];
        char[] chars = s.toCharArray();

        for (int i = 0; i < n - 1; i++) {
            if (chars[i] == chars[i + 1]) {
                update(i, 1);
            }
        }

        int resultCount = 0;
        for (int[] q : queries) {
            if (q[0] == 2) {
                resultCount++;
            }
        }

        int[] result = new int[resultCount];
        int k = 0;

        for (int[] q : queries) {
            if (q[0] == 1) {
                int index = q[1];
                
                if (index > 0) {
                    if (chars[index] == chars[index - 1]) {
                        update(index - 1, -1);
                    }
                }
                if (index < n - 1) {
                    if (chars[index] == chars[index + 1]) {
                        update(index, -1);
                    }
                }

                chars[index] = (chars[index] == 'A' ? 'B' : 'A');

                if (index > 0) {
                    if (chars[index] == chars[index - 1]) {
                        update(index - 1, 1);
                    }
                }
                if (index < n - 1) {
                    if (chars[index] == chars[index + 1]) {
                        update(index, 1);
                    }
                }
            } else {
                int l = q[1];
                int r = q[2];
                if (l >= r) {
                    result[k++] = 0;
                } else {
                    result[k++] = query(r - 1) - query(l - 1);
                }
            }
        }
        return result;
    }
}