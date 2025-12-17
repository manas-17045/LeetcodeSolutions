// Leetcode 3563: Lexicographically Smallest String After Adjacent Removals
// https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/
// Solved on 17th of December, 2025
class Solution {
    private Boolean[][] deleteMemo;
    private String[] solveMemo;
    private char[] chars;
    private int n;

    /**
     * Finds the lexicographically smallest string after performing adjacent removals.
     *
     * @param s The input string.
     * @return The lexicographically smallest string after removals.
     */
    public String lexicographicallySmallestString(String s) {
        n = s.length();
        chars = s.toCharArray();
        deleteMemo = new Boolean[n][n];
        solveMemo = new String[n + 1];
        return findSmallest(0);
    }

    private boolean canDelete(int i, int j) {
        if (i > j) {
            return true;
        }
        if (deleteMemo[i][j] != null) {
            return deleteMemo[i][j];
        }

        boolean result = false;
        if ((j - i + 1) % 2 == 0) {
            for (int k = i + 1; k <= j; k += 2) {
                if (isConsecutive(chars[i], chars[k]) && 
                    canDelete(i + 1, k - 1) && 
                    canDelete(k + 1, j)) {
                    result = true;
                    break;
                }
            }
        }
        deleteMemo[i][j] = result;
        return result;
    }

    private String findSmallest(int i) {
        if (i == n) {
            return "";
        }
        if (solveMemo[i] != null) {
            return solveMemo[i];
        }

        String smallest = chars[i] + findSmallest(i + 1);

        for (int k = i + 1; k < n; k += 2) {
            if (isConsecutive(chars[i], chars[k]) && canDelete(i + 1, k - 1)) {
                String candidate = findSmallest(k + 1);
                if (candidate.compareTo(smallest) < 0) {
                    smallest = candidate;
                }
            }
        }

        solveMemo[i] = smallest;
        return smallest;
    }

    private boolean isConsecutive(char a, char b) {
        int diff = Math.abs(a - b);
        return diff == 1 || diff == 25;
    }
}