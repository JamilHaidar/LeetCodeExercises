/*
 * Leetcode 238
 */

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];
        int mul = 1;
        for(int i=0;i<nums.length;i++){
            result[i] = mul;
            mul*=nums[i];
        }
        mul = 1;
        for(int i=nums.length-1;i>=0;i--){
            result[i]*=mul;
            mul*=nums[i];
        }
        return result;
    }
}