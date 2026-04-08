// Leetcode 3885: Design Event Manager
// https://leetcode.com/problems/design-event-manager/
// Solved on 8th of April, 2026
import java.util.Hashmap;
import java.util.Map;
import java.util.PriorityQueue;

class EventManager {

    private Map<Integer, Integer> priorityMap;
    private PriorityQueue<int[]> queue;

    public EventManager(int[][] events) {
        priorityMap = new HashMap<>();
        queue = new PriorityQueue<>((a, b) -> {
            if (a[0] == b[0]) {
                return Integer.compare(a[1], b[1]);
            }
            return Integer.compare(b[0], a[0]);
        });
        for (int[] event : events) {
            int id = event[0];
            int priority = event[1];
            priorityMap.put(id, priority);
            queue.offer(new int[]{priority, id});
        }
    }

    public void updatePriority(int eventId, int newPriority) {
        priorityMap.put(eventId, newPriority);
        queue.offer(new int[]{newPriority, eventId});
    }

    public int pollHighest() {
        while (!queue.isEmpty()) {
            int[] top = queue.poll();
            int priority = top[0];
            int id = top[1];
            if (priorityMap.containsKey(id) && priorityMap.get(id) == priority) {
                priorityMap.remove(id);
                return id;
            }
        }
        return -1;
    }
}