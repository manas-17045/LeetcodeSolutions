// Leetcode 321: Find X-Sum of All K-Long Subarrays II
// https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/
// Solved on 5th of November, 2025
class Solution {
    static class Entry {
        int val;
        int freq;

        Entry(int f, int v) {
            freq = f;
            val = v;
        }

        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Entry e = (Entry) o;
            return freq == e.freq && val == e.val;
        }

        public int hashCode() {
            return freq * 31 + val;
        }
    }

    /**
     * Finds the X-sum of all K-long subarrays. The X-sum is defined as the sum of values of the X most frequent elements in the subarray.
     * @param nums The input array of integers.
     * @param k The length of the subarrays.
     * @param x The number of most frequent elements to consider for the sum.
     * @return An array where each element is the X-sum of a K-long subarray.
     */
    public long[] findXSum(int[] nums, int k, int x) {
        int n = nums.length;
        int m = n - k + 1;
        long[] answer = new long[m];

        Comparator<Entry> comp = (a, b) -> {
            if (a.freq != b.freq) return Integer.compare(b.freq, a.freq);
            return Integer.compare(b.val, a.val);
        };

        TreeSet<Entry> top = new TreeSet<>(comp);
        TreeSet<Entry> rest = new TreeSet<>(comp);
        Map<Integer, Integer> freqMap = new HashMap<>();

        for (int i = 0; i < k; i++) {
            freqMap.put(nums[i], freqMap.getOrDefault(nums[i], 0) + 1);
        }

        for (Map.Entry<Integer, Integer> e : freqMap.entrySet()) {
            rest.add(new Entry(e.getValue(), e.getKey()));
        }

        long sumTop = 0;

        while (top.size() < x && !rest.isEmpty()) {
            Entry r = rest.pollFirst();
            top.add(r);
            sumTop += (long) r.freq * r.val;
        }

        while (!rest.isEmpty() && !top.isEmpty()) {
            Entry best = rest.first();
            Entry worst = top.last();
            if (comp.compare(best, worst) < 0) {
                rest.remove(best);
                top.remove(worst);
                sumTop -= (long) worst.freq * worst.val;
                top.add(best);
                sumTop += (long) best.freq * best.val;
                rest.add(worst);
            } else break;
        }

        while (top.size() > x) {
            Entry w = top.pollLast();
            sumTop -= (long) w.freq * w.val;
            rest.add(w);
        }

        answer[0] = sumTop;

        for (int i = k; i < n; i++) {
            int out = nums[i - k];
            int oldFreq = freqMap.getOrDefault(out, 0);

            if (oldFreq > 0) {
                Entry oldEntry = new Entry(oldFreq, out);
                if (top.remove(oldEntry)) sumTop -= (long) oldEntry.freq * oldEntry.val;
                else rest.remove(oldEntry);

                int newFreq = oldFreq - 1;
                if (newFreq == 0) freqMap.remove(out);
                else {
                    freqMap.put(out, newFreq);
                    rest.add(new Entry(newFreq, out));
                }
            }

            int in = nums[i];
            int prevFreq = freqMap.getOrDefault(in, 0);

            if (prevFreq > 0) {
                Entry prevEntry = new Entry(prevFreq, in);
                if (top.remove(prevEntry)) sumTop -= (long) prevEntry.freq * prevEntry.val;
                else rest.remove(prevEntry);
            }

            int newFreqIn = prevFreq + 1;
            freqMap.put(in, newFreqIn);
            rest.add(new Entry(newFreqIn, in));

            while (top.size() < x && !rest.isEmpty()) {
                Entry r = rest.pollFirst();
                top.add(r);
                sumTop += (long) r.freq * r.val;
            }

            while (!rest.isEmpty() && !top.isEmpty()) {
                Entry best = rest.first();
                Entry worst = top.last();
                if (comp.compare(best, worst) < 0) {
                    rest.remove(best);
                    top.remove(worst);
                    sumTop -= (long) worst.freq * worst.val;
                    top.add(best);
                    sumTop += (long) best.freq * best.val;
                    rest.add(worst);
                } else break;
            }

            while (top.size() > x) {
                Entry w = top.pollLast();
                sumTop -= (long) w.freq * w.val;
                rest.add(w);
            }

            answer[i - k + 1] = sumTop;
        }

        return answer;
    }
}