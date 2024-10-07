// Problem Name: 317. Letter Combinations of a Phone Number
// Problem Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution {
    public List<String> letterCombinations(String digits) {
        if(digits.length()==0) return List.of();

        HashMap<Character, char[]> numberToLettersMap = new HashMap<Character, char[]>();
        numberToLettersMap.put('2',new char[] {'a','b','c'});
        numberToLettersMap.put('3',new char[] {'d','e','f'});
        numberToLettersMap.put('4',new char[] {'g','h','i'});
        numberToLettersMap.put('5',new char[] {'j','k','l'});
        numberToLettersMap.put('6',new char[] {'m','n','o'});
        numberToLettersMap.put('7',new char[] {'p','q','r','s'});
        numberToLettersMap.put('8',new char[] {'t','u','v'});
        numberToLettersMap.put('9',new char[] {'w','x','y','z'});

        List<String> returnList=new ArrayList<>();
        backtrack("",digits,numberToLettersMap,returnList);
        return returnList;
    }
    private void backtrack(String combination,String subsequentDigits, HashMap<Character,char[]> numberToLettersMap,List<String> returnList){
        if(subsequentDigits.length()==0){
            returnList.add(combination);
        }
        else{
            for(char currentLetter : numberToLettersMap.get(subsequentDigits.charAt(0))){
                backtrack(combination+currentLetter,subsequentDigits.substring(1),numberToLettersMap,returnList);
            }
        }
    }
}
