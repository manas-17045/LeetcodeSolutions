// Leetcode 2402: Meeting Rooms III
// https://leetcode.com/problems/meeting-rooms-iii/
// Solved on 27th of December, 2025
import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public int mostBooked(int n, int[][] meetings) {
        Arrays.sort(meetings, (a, b) -> Integer.compare(a[0], b[0]));

        PriorityQueue<Integer> unusedRooms = new PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            unusedRooms.offer(i);
        }

        PriorityQueue<long[]> engagedRooms = new PriorityQueue<>((a, b) -> 
            a[0] != b[0] ? Long.compare(a[0], b[0]) : Long.compare(a[1], b[1])
        );

        int[] meetingCount = new int[n];

        for (int[] meeting : meetings) {
            int start = meeting[0];
            int end = meeting[1];

            while (!engagedRooms.isEmpty() && engagedRooms.peek()[0] <= start) {
                unusedRooms.offer((int) engagedRooms.poll()[1]);
            }

            if (!unusedRooms.isEmpty()) {
                int room = unusedRooms.poll();
                engagedRooms.offer(new long[]{end, room});
                meetingCount[room]++;
            } else {
                long[] current = engagedRooms.poll();
                long finishTime = current[0];
                int room = (int) current[1];
                long newEndTime = finishTime + (end - start);
                engagedRooms.offer(new long[]{newEndTime, room});
                meetingCount[room]++;
            }
        }

        int maxMeetings = 0;
        int resultRoom = 0;
        for (int i = 0; i < n; i++) {
            if (meetingCount[i] > maxMeetings) {
                maxMeetings = meetingCount[i];
                resultRoom = i;
            }
        }

        return resultRoom;
    }
}