// Leetcode 2284: Sender With Largest Word Count
// https://leetcode.com/problems/sender-with-largest-word-count/
// Solved on 16th of November, 2025
import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * Finds the sender with the largest word count. If multiple senders have the same largest word count,
     * the sender with the lexicographically largest name is returned.
     * @param messages An array of messages.
     * @param senders An array of senders, where senders[i] is the sender of messages[i].
     * @return The name of the sender with the largest word count.
     */
    public String largestWordCount(String[] messages, String[] senders) {
        Map<String, Integer> counts = new HashMap<>();
        String bestName = "";
        int bestCount = -1;
        for (int i = 0; i < messages.length; i++) {
            String msg = messages[i];
            String sender = senders[i];
            int words = 1;
            for (int j = 0; j < msg.length(); j++) if (msg.charAt(j) == ' ') words++;
            int total = counts.getOrDefault(sender, 0) + words;
            counts.put(sender, total);
            if (total > bestCount || (total == bestCount && sender.compareTo(bestName) > 0)) {
                bestCount = total;
                bestName = sender;
            }
        }
        return bestName;
    }
}