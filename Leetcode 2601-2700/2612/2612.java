// Leetcode 2612: Minimum Reverse Operations
// https://leetcode.com/problems/minimum-reverse-operations/
// Solved on 12th of November, 2025
import java.util.*;

class Solution {
    /**
     * Calculates the minimum number of reverse operations to move from position `p` to all other reachable positions.
     * A reverse operation involves choosing a subarray of length `k` and reversing it.
     *
     * @param n The total number of positions (0 to n-1).
     * @param p The starting position.
     * @param banned An array of positions that cannot be visited.
     * @param k The length of the subarray to be reversed in each operation.
     * @return An array where `answer[i]` is the minimum operations to reach position `i` from `p`, or -1 if unreachable.
     */
    public int[] minReverseOperations(int n, int p, int[] banned, int k) {
        boolean[] bannedFlag = new boolean[n];
        for (int b : banned) {
            bannedFlag[b] = true;
        }
        int[] answer = new int[n];
        Arrays.fill(answer, -1);
        answer[p] = 0;
        TreeSet<Integer> evenSet = new TreeSet<>();
        TreeSet<Integer> oddSet = new TreeSet<>();
        for (int i = 0; i < n; i++) {
            if (i == p || bannedFlag[i]) {
                continue;
            }
            if ((i & 1) == 0) {
                evenSet.add(i);
            } else {
                oddSet.add(i);
            }
        }
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        queue.add(p);
        while (!queue.isEmpty()) {
            int cur = queue.poll();
            int leftL = Math.max(0, cur - k + 1);
            int rightR = Math.min(cur, n - k);
            if (leftL > rightR) {
                continue;
            }
            int jmin = 2 * leftL + k - 1 - cur;
            int jmax = 2 * rightR + k - 1 - cur;
            TreeSet<Integer> useSet = ((jmin & 1) == 0) ? evenSet : oddSet;
            Integer next = useSet.ceiling(jmin);
            while (next != null && next <= jmax) {
                answer[next] = answer[cur] + 1;
                queue.add(next);
                useSet.remove(next);
                next = useSet.ceiling(jmin);
            }
        }
        return answer;
    }
}