// Problem Name: 77. Combinations
// Problem Link: https://leetcode.com/problems/combinations/description/

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
