// Leetcode 3816: Lexicographically Smallest String After Deleting Duplicate Characters
// https://leetcode.com/problems/lexicographically-smallest-string-after-deleting-duplicate-characters/
// Solved on 22nd of January, 2026
class solution {
    /**
     * Returns the lexicographically smallest string that can be formed by deleting
     * duplicate characters from the input string.
     * @param s The input string.
     * @return The lexicographically smallest string after deleting duplicate characters.
     */
    public String lexSmallestAfterDeletion(String s) {
        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
        }

        StringBuilder sb = new StringBuilder();
        int[] stackCount = new int[26];

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            count[c - 'a']--;

            while (sb.length() > 0 && sb.charAt(sb.length() - 1) > c) {
                char top = sb.charAt(sb.length() - 1);
                if (count[top - 'a'] > 0 || stackCount[top - 'a'] > 1) {
                    sb.deleteCharAt(sb.length() - 1);
                    stackCount[top - 'a']--;
                } else {
                    break;
                }
            }

            sb.append(c);
            stackCount[c - 'a']++;
        }

        while (sb.length() > 0) {
            char last = sb.charAt(sb.length() - 1);
            if (stackCount[last - 'a'] > 1) {
                sb.deleteCharAt(sb.length() - 1);
                stackCount[last - 'a']--;
            } else {
                break;
            }
        }

        return sb.toString();
    }
}