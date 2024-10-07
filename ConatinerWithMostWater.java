// Problem Name: 11. Container With Most Water
// Problem Link: https://leetcode.com/problems/container-with-most-water/description/

class Solution {
    public int maxArea(int[] height) {
        int smallPointer=0;
        int largePointer=height.length-1;
        int maxWater=0;
        while (largePointer > smallPointer) {
            maxWater=Math.max(maxWater,Math.min(height[largePointer],height[smallPointer])*(largePointer-smallPointer));
            if (height[largePointer] > height[smallPointer]){
                smallPointer++;
            }
            else{
                largePointer--;
            }
        }
        return maxWater;
    }
}
