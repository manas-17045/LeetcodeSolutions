// Leetcode 3680: Generate Schedule
// https://leetcode.com/problems/generate-schedule/
// Solved on 28th of December, 2025
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    /**
     * Generates a schedule of matches for `n` participants.
     *
     * @param n The number of participants.
     * @return A 2D array representing the schedule, where each inner array `[u, v]` denotes a match between participant `u` and participant `v`. Returns an empty 2D array if no valid schedule can be generated (e.g., for `n <= 4` or after multiple attempts).
     */
    public int[][] generateSchedule(int n) {
        if (n <= 4) {
            return new int[0][0];
        }

        int m = (n % 2 == 1) ? n + 1 : n;
        List<List<int[]>> baseRounds = new ArrayList<>();

        for (int r = 0; r < m - 1; r++) {
            List<int[]> round = new ArrayList<>();
            for (int i = 0; i < m / 2; i++) {
                int a = (r + i) % (m - 1);
                int b = (m - 1 + r - i) % (m - 1);
                int u, v;
                if (i == 0) {
                    u = m - 1;
                    v = a;
                } else {
                    u = a;
                    v = b;
                }
                if (u < n && v < n) {
                    round.add(new int[]{u, v});
                }
            }
            if (!round.isEmpty()) {
                baseRounds.add(round);
            }
        }

        List<List<int[]>> allRounds = new ArrayList<>();
        for (List<int[]> r : baseRounds) {
            List<int[]> forward = new ArrayList<>();
            List<int[]> backward = new ArrayList<>();
            for (int[] match : r) {
                forward.add(new int[]{match[0], match[1]});
                backward.add(new int[]{match[1], match[0]});
            }
            allRounds.add(forward);
            allRounds.add(backward);
        }

        for (int attempt = 0; attempt < 500; attempt++) {
            Collections.shuffle(allRounds);
            List<int[]> schedule = new ArrayList<>();
            boolean valid = true;

            for (List<int[]> round : allRounds) {
                List<int[]> current = new ArrayList<>(round);
                Collections.shuffle(current);

                if (schedule.isEmpty()) {
                    schedule.addAll(current);
                    continue;
                }

                int[] last = schedule.get(schedule.size() - 1);
                int idx = -1;

                for (int i = 0; i < current.size(); i++) {
                    int[] next = current.get(i);
                    if (last[0] != next[0] && last[0] != next[1] &&
                        last[1] != next[0] && last[1] != next[1]) {
                        idx = i;
                        break;
                    }
                }

                if (idx != -1) {
                    schedule.add(current.get(idx));
                    for (int i = 0; i < current.size(); i++) {
                        if (i != idx) {
                            schedule.add(current.get(i));
                        }
                    }
                } else {
                    valid = false;
                    break;
                }
            }

            if (valid) {
                int[][] result = new int[schedule.size()][2];
                for (int i = 0; i < schedule.size(); i++) {
                    result[i] = schedule.get(i);
                }
                return result;
            }
        }

        return new int[0][0];
    }
}