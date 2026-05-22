// Leetcode 3921: Score validator
// https://leetcode.com/probblems/score-validator/
// Solved on 22nd of May, 2026
class Solution {
    /**
     * Validates and calculates the total score and wicket count based on a series of events.
     *
     * @param events An array of strings representing match events (e.g., "W" for wicket, "WD"/"NB" for extras, or digit strings for runs).
     * @return An integer array where the first element is the total score and the second is the total wickets.
     */
    public int[] scoreValidator(String[] events) {
        int score = 0;
        int counter = 0;
        for (String event : events) {
            if (event.equals("W")) {
                counter++;
            } else if (event.equals("WD") || event.equals("NB")) {
                score++;
            } else {
                score += event.charAt(0) - '0';
            }
            if (counter == 10) {
                break;
            }
        }
        return new int[]{score, counter};
    }
}