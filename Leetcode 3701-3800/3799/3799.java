// Leetcode 3799: Word Squares II
// https://leetcode.com/problems/word-squares-ii/
// Solved on 9th of January, 2026
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    /**
     * Finds all word squares that can be formed by the given list of words.
     * A word square is a sequence of words such that the k-th row and k-th column read the same string.
     * @param words An array of strings from which to form word squares.
     * @return A list of lists of strings, where each inner list represents a valid word square.
     */
    public Lisr<List<String>> wordSquares(String[] words) {
        Arrays.sort(words);
        List<List<String>> result = new ArrayList<>();
        int n = words.length;

        for (int i = 0; i < n; i++) {
            String top = words[i];
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    continue;
                }
                String left = words[j];
                if (top.charAt(0) != left.charAt(0)) {
                    continue;
                }

                for (int k = 0; k < n; k++) {
                    if (k == i || k == j) {
                        continue;
                    }
                    String right = words[k];
                    if (top.charAt(3) != right.charAt(0)) {
                        continue;
                    }

                    for (int l = 0; l < n; l++) {
                        if (l == i || l == j || l == k) {
                            continue;
                        }
                        String bottom = words[l];
                        if (bottom.charAt(0) != left.charAt(3)) {
                            continue;
                        }
                        if (bottom.charAt(3) != right.charAt(3)) {
                            continue;
                        }

                        List<String> square = new ArrayList<>();
                        square.add(top);
                        square.add(left);
                        square.add(right);
                        square.add(bottom);
                        result.add(square);
                    }
                }
            }
        }
        return result;
    }
}