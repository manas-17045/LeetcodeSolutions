// Leetcode 2409: Count Days Spent Together
// https://leetcode.com/problems/count-days-spent-together/
// Solved on 24th of October, 2026
class Solution {
    /**
     * Calculates the total number of days Alice and Bob are in Rome together.
     *
     * @param arriveAlice the arrival date of Alice in MM-DD format
     * @param leaveAlice the departure date of Alice in MM-DD format
     * @param arriveBob the arrival date of Bob in MM-DD format
     * @param leaveBob the departure date of Bob in MM-DD format
     * @return the total number of overlapping days spent in Rome
     */
    public int countDaysTogether(String arriveAlic, String leaveAlice, String arriveBob, String leaveBob) {
        String latestArrival = arriveAlice.compareTo(arriveBob) >= 0 ? arriveAlice : arriveBob;
        String earliestDeparture = leaveAlice.compareTo(leaveBob) <= 0 ? leaveAlice : leaveBob;

        if (latestArrival.compareTo(earliestDeparture) > 0) {
            return 0;
        }

        int[] daysPerMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        int startMonth = (latestArrival.charAt(0) - '0') * 10 + (latestArrival.charAt(1) - '0');
        int startDay = (latestArrival.charAt(3) - '0') * 10 + (latestArrival.charAt(4) - '0');
        int endMonth = (earliestDeparture.charAt(0) - '0') * 10 + (earliestDeparture.charAt(1) - '0');
        int endDay = (earliestDeparture.charAt(3) - '0') * 10 + (earliestDeparture.charAt(4) - '0');

        int startDayOfYear = startDay;
        for (int i = 0; i < startMonth - 1; i++) {
            startDayOfYear += daysPerMonth[i];
        }

        int endDayOfYear = endDay;
        for (int i = 0; i < endMonth - 1; i++) {
            endDayOfYear += daysPerMonth[i];
        }

        return endDayOfYear - startDayOfYear + 1;
    }
}