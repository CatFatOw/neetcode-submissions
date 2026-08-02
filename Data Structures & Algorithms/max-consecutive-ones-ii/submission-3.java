class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max_ones = 0;
        int curr_ones = 0;
        int left = 0;
        int flipped = 0;

        for (int right = 0; right < nums.length; right++){
            if (nums[right] == 1){
                curr_ones ++;
            }

            if (nums[right] == 0){
                flipped ++;
                curr_ones ++;
            }

            while (flipped > 1){
                if (nums[left] == 0){
                    flipped -=1;
                }
                curr_ones -= 1;
                left += 1;
            }
            max_ones = Math.max(max_ones, curr_ones);
        }
        return max_ones;
    }
}
