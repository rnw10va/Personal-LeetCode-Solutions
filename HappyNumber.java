// Problem Name: 202. Happy Number
// Problem Link: https://leetcode.com/problems/happy-number/description/

class Solution {
    public boolean isHappy(int n) {
        Map<Integer,Integer> map = new HashMap<Integer,Integer>();
        while(n!=1){
            if(map.containsKey(n)){
                return false;
            }
            map.put(n,null);
            int tempN=n;
            n=0;
            while(tempN > 9){
                n+=Math.pow(tempN%10,2);
                tempN=Math.floorDiv(tempN,10);
            }
            n+=Math.pow(tempN%10,2);
        }
        return true;
    }
}
