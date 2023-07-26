import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public String[] solution(String[] quiz) {
        List<String> answer = new ArrayList<>();
        String[][] quizList = new String[quiz.length][2];
        
        for (int i = 0; i < quiz.length; i++) {
            quizList[i] = quiz[i].split(" = ");
        }
        
        for (String[] q : quizList) {
            String[] ex = q[0].split(" ");
            int a = Integer.parseInt(ex[0]);
            int b = Integer.parseInt(ex[2]);
            int c = Integer.parseInt(q[1]);
            
            if (ex[1].equals("+")) {
                if (a + b == c) {
                    answer.add("O");
                } else {
                    answer.add("X");
                }
            } else {
                if (a - b == c) {
                    answer.add("O");
                } else {
                    answer.add("X");
                }
            }
        }
        
        return answer.toArray(new String[0]);
    }
}