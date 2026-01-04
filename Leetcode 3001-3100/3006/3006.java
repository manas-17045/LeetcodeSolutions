// Leetcode 3006: Find Beautiful Indices in the Given Array I
// https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/
// Solved on 4th of January, 2026
import java.util.ArrayList;
import java.util.List;

class Solution {
    /**
     * Finds all "beautiful" indices in a given string `s`.
     * An index `i` is beautiful if `s` contains string `a` starting at `i`,
     * and there exists an index `j` such that `s` contains string `b` starting at `j`,
     * and `|i - j| <= k`.
     * @param s The main string to search within.
     * @param a The first substring to find.
     * @param b The second substring to find.
     * @param k The maximum allowed absolute difference between the starting indices of `a` and `b`.
     * @return A list of all beautiful indices.
     */
    public List<Integer> beautifulIndices(String s, String a, String b, int k) {
        List<Integer> indicesA = new ArrayList<>();
        List<Integer> indicesB = new ArrayList<>();
        List<Integer> result = new ArrayList<>();
        
        int lenS = s.length();
        int lenA = a.length();
        int lenB = b.length();

        for (int i = 0; i <= lenS - lenA; i++) {
            if (s.startsWith(a, i)) {
                indicesA.add(i);
            }
        }

        for (int i = 0; i <= lenS - lenB; i++) {
            if (s.startsWith(b, i)) {
                indicesB.add(i);
            }
        }

        int j = 0;
        for (int i : indicesA) {
            while (j < indicesB.size() && indicesB.get(j) < i - k) {
                j++;
            }
            if (j < indicesB.size() && Math.abs(indicesB.get(j) - i) <= k) {
                result.add(i);
            }
        }

        return result;
    }
}