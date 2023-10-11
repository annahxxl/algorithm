package 김태원.초급.자료구조_활용.겹쳐진_압축_해제;

import java.util.*;

class Solution {
    public String solution(String s) {
        Stack<String> stack = new Stack<>();

        for (Character x : s.toCharArray()) {
            if (x == ')') {
                String str = "";

                while (!stack.isEmpty()) {
                    String c = stack.pop();

                    if (c.equals("(")) {
                        String num = "";
                        while (!stack.isEmpty() && Character.isDigit(stack.peek().charAt(0))) {
                            num = stack.pop() + num;
                        }

                        int cnt = num.equals("") ? 1 : Integer.parseInt(num);

                        String res = "";
                        for (int i = 0; i < cnt; i++) {
                            res += str;
                        }

                        stack.push(res);
                        break;
                    }

                    str = c + str;
                }
            } else {
                stack.push(String.valueOf(x));
            }
        }

        String answer = "";
        for (String str : stack) {
            answer += str;
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution T = new Solution();
        System.out.println(T.solution("3(a2(b))ef"));
        System.out.println(T.solution("2(ab)k3(bc)"));
        System.out.println(T.solution("2(ab3((cd)))"));
        System.out.println(T.solution("2(2(ab)3(2(ac)))"));
        System.out.println(T.solution("3(ab2(sg))"));
    }
}
