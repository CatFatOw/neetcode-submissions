class Solution {
    public int minimumDifference(int[] nums, int k) {
        Arrays.sort(nums);
        int min_difference = Integer.MAX_VALUE;

        int right = k-1;
        min_difference = Math.min(min_difference, nums[right]-nums[0]);

        for (right = k; right < nums.length; right++){
            min_difference = Math.min(min_difference, nums[right]-nums[right-k+1]);
        }
        return min_difference;


        
    }
}