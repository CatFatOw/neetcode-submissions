class Solution {
    public String mergeAlternately(String word1, String word2) {

        int ptr1 = 0;
        int ptr2 = 0;
        int counter = 0;
        StringBuilder result = new StringBuilder();

        while (ptr1 < word1.length() && ptr2 < word2.length()){
            if (counter % 2 == 0){
                result.append(word1.charAt(ptr1));
                ptr1 ++;

            }
            else{
                result.append(word2.charAt(ptr2));
                ptr2++;
            }
            counter++;

        }

        while (ptr1 < word1.length()){
            result.append(word1.charAt(ptr1));
            ptr1++;
        }

        while (ptr2< word2.length()){
            result.append(word2.charAt(ptr2));
            ptr2++;
        }

        String word = result.toString();
        return word;
        
    }
}