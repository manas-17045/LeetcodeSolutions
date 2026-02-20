// Leetcode 761: Special Binary String
// https://leetcode.com/problems/special-binary-string/
// Solved on 20th of February, 2026
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    /**
     * Reorders the special binary string to make it lexicographically largest.
     *
     * @param s A special binary string.
     * @return The lexicographically largest special binary string after swapping.
     */
    public String makeLargestSpecial(String s) {
        int count = 0;
        int start = 0;
        List<String> specialStrings = new ArrayList<>();

        for (int end = 0; end < s.length(); end++) {
            if (s.charAt(end) == '1') {
                count++;
            } else {
                count--;
            }

            if (count == 0) {
                String innerString = makeLargestSpecial(s.substring(start + 1, end));
                specialStrings.add("1" + innerString + "0");
                start = end + 1;
            }
        }

        Collections.sort(specialStrings, Collections.reverseOrder());
        return String.join("", specialStrings);
    }
}