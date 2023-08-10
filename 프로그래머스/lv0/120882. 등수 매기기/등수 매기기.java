import java.util.*;

class Solution {
    public int[] solution(int[][] score) {
        List<Integer> totalScores = new ArrayList<>();
        for (int[] s : score) {
            totalScores.add(s[0] + s[1]);
        }
        
        totalScores.sort(Comparator.reverseOrder());

        int[] answer = new int[score.length];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = totalScores.indexOf(score[i][0] + score[i][1]) + 1;
        }
        
        return answer;
    }
}