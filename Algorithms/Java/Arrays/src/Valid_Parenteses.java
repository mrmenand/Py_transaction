
class Solution {
	public boolean isValid(String s){
//		Stack<Character> stack = new Stack<>();
		ArrayStack<Character>  stack = new ArrayStack<>();
		for(int i = 0 ;i < s.length();i ++){
			char c = s.charAt(i);
			if( c =='(' || c == '[' || c == '{')
				stack.push(c);
			else{
				if(stack.isEmpty())
					return false;

				char Topchar = stack.pop();
				if(c==')' && Topchar != '(')
					return false;
				if(c==']' && Topchar !='[')
					return  false;
				if(c=='}' && Topchar != '{')
					return false;
			}
		}
		return  stack.isEmpty();
	}

	public static void main(String[] args) {

		System.out.println((new Solution()).isValid("()[]{}"));
		System.out.println((new Solution()).isValid("([)]"));
	}
}