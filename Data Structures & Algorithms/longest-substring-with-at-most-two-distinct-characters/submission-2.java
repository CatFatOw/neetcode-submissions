class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        int longest = 0;
        int left = 0;

        HashMap<Character, Integer> mapping = new HashMap<>();

        for (int right = 0; right < s.length(); right++) {
            char rightChar = s.charAt(right);

            mapping.put(
                rightChar,
                mapping.getOrDefault(rightChar, 0) + 1
            );

            while (mapping.size() > 2) {
                char leftChar = s.charAt(left);

                mapping.put(
                    leftChar,
                    mapping.get(leftChar) - 1
                );

                if (mapping.get(leftChar) == 0) {
                    mapping.remove(leftChar);
                }

                left++;
            }

            longest = Math.max(longest, right - left + 1);
        }

        return longest;
    }
}