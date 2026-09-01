class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        String operations = "+-*/";
        int result = 0;

        for (String s : tokens){
            if (!operations.contains(s))
                stack.push(Integer.parseInt(s));
            else if (s.equals("+")){
                //System.out.println(stack.toString() + ": +");
                result = stack.pop();
                result += stack.pop();
                stack.push(result);
            }
            else if (s.equals("*")){
                //System.out.println(stack.toString() + ": +");
                result = stack.pop();
                result *= stack.pop();
                stack.push(result);
            }
            else if (s.equals("-")){
                //System.out.println(stack.toString() + ": +");
                result = stack.pop();
                result = stack.pop() - result;
                stack.push(result);
            }
            else if (s.equals("/")){
                //System.out.println(stack.toString() + ": +");
                result = stack.pop();
                if (stack.peek() != 0)
                    result = stack.pop() / result;
                else
                    result = 0;
                stack.push(result);
            }
            
        }

        return stack.pop();
    }
}
