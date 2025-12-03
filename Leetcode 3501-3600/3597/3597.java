// Leetcode 3597: Partition String
// https://leetcode.com/problems/partition-string/
// Solved on 3rd of December, 2025
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    /**
     * Partitions a given string `s` into the smallest possible number of substrings such that each character appears in at most one substring.
     *
     * @param s The input string to be partitioned.
     * @return A list of strings representing the partitioned segments.
     */
    public List<String> partitionString(String s) {
        List<String> segments = new ArrayList<>();
        Set<String> seenSegments = new HashSet<>();
        int length = s.length();
        int index = 0;

        while (index < length) {
            StringBuilder currentSegment = new StringBuilder();
            currentSegment.append(s.charAt(index));
            index++;

            while (seenSegments.contains(currentSegment.toString())) {
                if (index >= length) {
                    return segments;
                }
                currentSegment.append(s.charAt(index));
                index++;
            }

            String uniqueSegment = currentSegment.toString();
            seenSegments.add(uniqueSegment);
            segments.add(uniqueSegment);
        }

        return segments;
    }
}