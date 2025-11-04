// Leetcode 3295: Report Spam Message
// https://leetcode.com/problems/report-spam-message/
// Solved on 4th of November, 2025
import java.util.HashSet;

class Solution {
    /**
     * Reports whether a message is spam based on a list of banned words.
     * @param message The message as an array of strings (words).
     * @param bannedWords An array of strings representing words that are considered spam.
     * @return True if two or more words in the message are found in the bannedWords list, false otherwise.
     */
    public boolean reportSpam(String[] message, String[] bannedWords) {
        HashSet<String> bannedSet = new HashSet<>(Math.max(16, bannedWords.length * 2));
        for (String w : bannedWords) {
            bannedSet.add(w);
        }
        int matchCount = 0;
        for (String s : message) {
            if (bannedSet.contains(s) && ++matchCount >= 2) {
                return true;
            }
        }
        return false;
    }
}