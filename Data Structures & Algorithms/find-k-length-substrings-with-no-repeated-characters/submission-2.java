class Solution {
    public int numKLenSubstrNoRepeats(String s, int k) {
        if (k > s.length()) {
            return 0;
        }

        HashMap<Character, Integer> mapping = new HashMap<>();
        int total = 0;

        // Build the first window.
        for (int i = 0; i < k; i++) {
            char c = s.charAt(i);
            mapping.put(c, mapping.getOrDefault(c, 0) + 1);
        }

        if (mapping.size() == k) {
            total++;
        }

        // Slide the window.
        for (int i = k; i < s.length(); i++) {
            char leaving = s.charAt(i - k);

            mapping.put(leaving, mapping.get(leaving) - 1);

            if (mapping.get(leaving) == 0) {
                mapping.remove(leaving);
            }

            char entering = s.charAt(i);
            mapping.put(entering, mapping.getOrDefault(entering, 0) + 1);

            if (mapping.size() == k) {
                total++;
            }
        }

        return total;
    }
}