// Leetcode 3016: Minimum Number of Pushes to Type Word II
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/
// Solved on 7th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum number of pushes required to type a given word on a phone keypad.
     * @param word The input word to type.
     * @return The minimum number of pushes.
     */
    public int minimumPushes(String word) {
        int[] freq = new int[26];
        for (int i = 0; i < word.length(); i++) {
            freq[word.charAt(i) - 'a']++;
        }
        Arrays.sort(freq);
        long total = 0;
        int count = 0;
        for (int i = 25; i >= 0; i--) {
            if (freq[i] == 0){
                continue;
            }
            int position = count / 8 + 1;
            total += (long) freq[i] * position;
            count++;
        }
        return (int) total;
    }
}