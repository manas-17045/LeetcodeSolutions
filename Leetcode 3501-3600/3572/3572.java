// Leetcode 3572: Maximize Y-Sum by Picking a Triplet of Distinct X-Values
// https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/
// Solved on 7th of November, 2025
import java.util.*;

class Solution {
    /**
     * Calculates the maximum Y-sum by picking a triplet of distinct X-values.
     * @param x An array of X-coordinates.
     * @param y An array of Y-coordinates.
     * @return The maximum Y-sum, or -1 if no such triplet can be formed.
     */
    public int maxSumDistinctTriplet(int[] x, int[] y) {
        int n = x.length;
        HashMap<Integer,int[]> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int xi = x[i];
            int yi = y[i];
            int[] arr = map.get(xi);
            if (arr == null) {
                arr = new int[4];
                map.put(xi, arr);
            }
            int count = arr[0];
            if (yi > arr[1]) {
                arr[3] = arr[2];
                arr[2] = arr[1];
                arr[1] = yi;
                if (count < 3) {
                    arr[0] = count + 1;
                }
            } else if (yi > arr[2]) {
                arr[3] = arr[2];
                arr[2] = yi;
                if (count < 3) {
                    arr[0] = count + 1;
                }
            } else if (yi > arr[3]) {
                arr[3] = yi;
                if (count < 3) {
                    arr[0] = count + 1;
                }
            }
        }
        if (map.size() < 3) {
            return -1;
        }
        ArrayList<int[]> list = new ArrayList<>();
        for (Map.Entry<Integer,int[]> e : map.entrySet()) {
            int key = e.getKey();
            int[] v = e.getValue();
            int c = v[0];
            for (int i = 1; i <= c; i++) {
                list.add(new int[]{v[i], key});
            }
        }
        list.sort((a,b) -> Integer.compare(b[0], a[0]));
        HashSet<Integer> used = new HashSet<>();
        int sum = 0;
        for (int[] p : list) {
            if (used.contains(p[1])){
                continue;
            }
            used.add(p[1]);
            sum += p[0];
            if (used.size() == 3){
                break;
            }
        }
        return used.size() == 3 ? sum : -1;
    }
}