/* 
Problem Name: 77. Combinations
Problem Link: https://leetcode.com/problems/combinations/description/
Problem Description:
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.


Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.


Constraints:
    1 <= n <= 20
    1 <= k <= n
*/ 

// My Solution
class Solution {
    public List<List<Integer>> combine(int n, int k) {
        if(k==1){
            List<List<Integer>> returnList = new ArrayList<List<Integer>>();
            for(int i=1;i<=n;i++){
                returnList.add(new ArrayList<Integer>(List.of(i)));
            }
            return returnList;
        }
        return recursion(n,k-1);
    }

    private List<List<Integer>> recursion(int maxOfRange,int recursionsCallsLeft){
        List<List<Integer>> returnList = new ArrayList<List<Integer>>();
        if(recursionsCallsLeft==0){
            for(int i=1;i<=maxOfRange-1;i++){
                returnList.add(new ArrayList<Integer>(List.of(i)));
            }
            return returnList;
        }
        else{
            List<List<Integer>> tempList=recursion(maxOfRange,recursionsCallsLeft-1);
            for(int i=1;i<=maxOfRange;i++){
                for(int j=0;j<tempList.size();j++){
                    if(i>tempList.get(j).get(tempList.get(j).size()-1)){
                        List<Integer> tempValList=new ArrayList<Integer>(tempList.get(j));
                        tempValList.add(i);
                        returnList.add(tempValList);
                    }
                }
            } 
            return returnList;
        }
    }
}