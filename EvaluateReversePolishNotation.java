// Problem Name: 150. Evaluate Reverse Polish Notation
// Problem Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

class Solution {
    public int evalRPN(String[] tokens) {
        int first,second;
        Stack<Integer> stack = new Stack<>();
        for(String token : tokens){
            if(token.equals("+")){
                stack.add(stack.pop()+stack.pop());
            }
            else if(token.equals("-")){
                second = stack.pop();
                first = stack.pop();
                stack.add(first-second);
            }
            else if(token.equals("*")){
                stack.add(stack.pop()*stack.pop());
            }
            else if(token.equals("/")){
                second = stack.pop();
                first = stack.pop();
                stack.add(first/second);
            }
            else{
                stack.add(Integer.parseInt(token));
            }
        }
    return stack.pop();
    }
}
