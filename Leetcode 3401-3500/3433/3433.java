// Leetcode 3433: Count Mentions Per User
// https://leetcode.com/problems/count-mentions-per-user/
// Solved on 10th of December, 2025
import java.util.Collections;
import java.util.List;

class Solution {
    /**
     * Counts the number of mentions for each user based on a list of events.
     * @param numberOfUsers The total number of users.
     * @param events A list of events, where each event is a list of strings.
     * @return An array where the i-th element is the number of mentions for user i.
     */
    public int[] countMentions(int numberOfUsers, List<List<String>> events) {
        Collections.sort(events, (a, b) -> {
            int timeA = Integer.parseInt(a.get(1));
            int timeB = Integer.parseInt(b.get(1));
            if (timeA != timeB) {
                return timeA - timeB;
            }
            boolean isOfflineA = a.get(0).equals("OFFLINE");
            boolean isOfflineB = b.get(0).equals("OFFLINE");
            if (isOfflineA == isOfflineB) {
                return 0;
            }
            return isOfflineA ? -1 : 1;
        });

        int[] mentions = new int[numberOfUsers];
        int[] onlineTime = new int[numberOfUsers];

        for (List<String> event : events) {
            String type = event.get(0);
            int timestamp = Integer.parseInt(event.get(1));

            if (type.equals("OFFLINE")) {
                int id = Integer.parseInt(event.get(2));
                onlineTime[id] = timestamp + 60;
            } else {
                String target = event.get(2);
                if (target.equals("ALL")) {
                    for (int i = 0; i < numberOfUsers; i++) {
                        mentions[i]++;
                    }
                } else if (target.equals("HERE")) {
                    for (int i = 0; i < numberOfUsers; i++) {
                        if (timestamp >= onlineTime[i]) {
                            mentions[i]++;
                        }
                    }
                } else {
                    String[] tokens = target.split(" ");
                    for (String token : tokens) {
                        int id = Integer.parseInt(token.substring(2));
                        mentions[id]++;
                    }
                }
            }
        }
        return mentions;
    }
}