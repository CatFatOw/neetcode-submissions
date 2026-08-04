class Solution {
    public boolean checkInclusion(String s1, String s2) {
        HashMap<Character, Integer> s1_mapping = new HashMap<>();
        HashMap<Character, Integer> mapping = new HashMap<>();

        if (s1.length() > s2.length()){
            return false;
        }

        // populate the s1 mapping first
        for (int i = 0; i < s1.length();i++){
            if (s1_mapping.containsKey(s1.charAt(i))){
                s1_mapping.put(s1.charAt(i), s1_mapping.get(s1.charAt(i)) + 1);
            }else{
                s1_mapping.put(s1.charAt(i), 1);
            }
        }

        // do a fixed sliding window approaach
        int k = s1.length();

        for (int i =0; i < k; i++){
            if (mapping.containsKey(s2.charAt(i))){
                mapping.put(s2.charAt(i), mapping.get(s2.charAt(i)) + 1);
            }else{
                mapping.put(s2.charAt(i), 1);
            }
        }

        if (s1_mapping.equals(mapping)){
            return true;
        }

        for (int i = k; i < s2.length(); i++){
            mapping.put(
                s2.charAt(i - k),
                mapping.get(s2.charAt(i - k)) - 1
            );
            if (mapping.get(s2.charAt(i-k)) == 0){
                mapping.remove(s2.charAt(i-k));
            }

            if (mapping.containsKey(s2.charAt(i))){
                mapping.put(s2.charAt(i), mapping.get(s2.charAt(i)) + 1);
            }else{
                mapping.put(s2.charAt(i), 1);
            }

            if (mapping.equals(s1_mapping)){
                return true;
            }
        }
        return false;

    }
}