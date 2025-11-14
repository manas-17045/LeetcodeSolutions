// Leetcode 1904: The Number of Full Rounds You Have Played
// https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/
// Solved on 14th of November, 2025
class Solution {
    /**
     * Calculates the number of full 15-minute rounds played between a login and logout time.
     * @param loginTime The login time in "HH:MM" format.
     * @param logoutTime The logout time in "HH:MM" format.
     * @return The number of full 15-minute rounds played.
     */
    public int numberOfRounds(String loginTime, String logoutTime) {
        String[] lp = loginTime.split(":");
        String[] rp = logoutTime.split(":");
        int lh = Integer.parseInt(lp[0]);
        int lm = Integer.parseInt(lp[1]);
        int rh = Integer.parseInt(rp[0]);
        int rm = Integer.parseInt(rp[1]);
        int start = lh * 60 + lm;
        int end = rh * 60 + rm;
        if (end < start) {
            end += 24 * 60;
        }
        int firstIndex = (start + 14) / 15;
        int lastIndex = end >= 15 ? (end - 15) / 15 : -1;
        int res = lastIndex - firstIndex + 1;
        return res > 0 ? res : 0;
    }
}