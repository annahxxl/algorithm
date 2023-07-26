import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public String[] solution(String[] quiz) {
        List<String> answer = new ArrayList<>();
        
        for (String q : quiz) {
            String[] splitQuiz = q.split(" = ");
            String[] ex = splitQuiz[0].split(" ");
            
            int a = Integer.parseInt(ex[0]);
            String operator = ex[1];
            int b = Integer.parseInt(ex[2]);
            int c = Integer.parseInt(splitQuiz[1]);
            
            boolean isCorrect = operator.equals("+") ? a + b == c : a - b == c;
            
            answer.add(isCorrect ? "O" : "X");
        }
        
        return answer.toArray(new String[0]);
    }
}