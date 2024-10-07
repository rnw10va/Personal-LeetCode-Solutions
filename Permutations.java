// Problem Name: 46. Permutations
// Problem Link: https://leetcode.com/problems/permutations/description/

class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> returnList=new ArrayList<>();
        recursion(returnList,new ArrayList<>(),nums);
        return returnList;
    }
    private void recursion(List<List<Integer>> returnList,List<Integer> comboSoFar,int[] numsRemaining){
        if(numsRemaining.length==1){
            comboSoFar.add(numsRemaining[0]);
            returnList.add(comboSoFar);
        }
        else{
            int lengthOfNumsRemaining=numsRemaining.length;
            for(int i=0;i<lengthOfNumsRemaining;i++){
                List<Integer> returnListList=new ArrayList<>(comboSoFar);
                returnListList.add(numsRemaining[i]);
                int[] newNumsRemaining=new int[lengthOfNumsRemaining-1];
                int k=0;
                for(int j=0;j<lengthOfNumsRemaining;j++){
                    if(j!=i){
                        newNumsRemaining[k]=numsRemaining[j];
                        k++;
                    }
                }
                recursion(returnList,returnListList,newNumsRemaining);
            }  
        }
    }
}
