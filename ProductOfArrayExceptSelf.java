// Problem Name: 238. Product of Array Except Self
// Problem Link: https://leetcode.com/problems/product-of-array-except-self/description/

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int sum=1;
        int zeroCount=0;
        for(int num : nums){
            if(num!=0){
                sum*=num;
            }
            else{
                zeroCount++;
            }
        }
        if(zeroCount>1){
            for(int i=0;i<nums.length;i++){
                nums[i]=0;
            }
        }
        else if(zeroCount==1){
            for(int i=0;i<nums.length;i++){
                if(nums[i]!=0){
                    nums[i]=0;
                }
                else{
                    nums[i]=sum; 
                }  
            }
        }
        else{
            for(int i=0;i<nums.length;i++){
                nums[i]=sum/nums[i];
            }
        }
        return nums; 
    }
}
