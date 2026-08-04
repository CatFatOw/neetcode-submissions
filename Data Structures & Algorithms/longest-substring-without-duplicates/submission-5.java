class Solution {
    public int lengthOfLongestSubstring(String s) {

        HashMap<Character, Integer> mapping = new HashMap<>();
        int longest = 0;
        int curr = 0;
        int left = 0;

        for (int right = 0; right < s.length(); right++){
            if (mapping.containsKey(s.charAt(right))){
                mapping.put(s.charAt(right), mapping.get(s.charAt(right))+1);
            }
            else {
                mapping.put(s.charAt(right), 1);
            }

            while (mapping.get(s.charAt(right)) > 1){
                mapping.put(s.charAt(left), mapping.get(s.charAt(left))-1);
                if (mapping.get(s.charAt(left)) <= 0){
                    mapping.remove(s.charAt(left));
                }
                left ++;

            }
            longest = Math.max(longest, right-left+1);
        }
        return longest;


    }
}
