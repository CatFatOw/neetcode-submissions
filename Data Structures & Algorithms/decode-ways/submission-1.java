class Solution {
    public int numDecodings(String s) {

        HashMap<Integer, Integer> memo = new HashMap<>();
        return dp(s.length()-1, memo, s);


        
    }

    public int dp(int idx, HashMap<Integer, Integer> memo, String s){
        if (idx < 0){
            return 1;
        }

        if (memo.containsKey(idx)){
            return memo.get(idx);
        }

        int total = 0;
        int oneDigit = s.charAt(idx) - '0';


        if (oneDigit >= 1 && oneDigit <= 9) {
            total += dp(idx-1, memo, s);
        }

        if (idx >= 1) {
            int twoDigits = Integer.parseInt(s.substring(idx - 1, idx + 1));

            if (twoDigits >= 10 && twoDigits <= 26) {
                total += dp(idx - 2, memo, s);
            }
        }

        memo.put(idx, total);
        return total;
    }
}
