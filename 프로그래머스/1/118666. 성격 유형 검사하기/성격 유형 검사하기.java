import java.util.*;

class Solution {
    public String solution(String[] survey, int[] choices) {
        Map<Character, Integer> scores = new HashMap<>();
        
        for (int i = 0; i < survey.length; i++) {
            int choice = choices[i];
            char[] types = survey[i].toCharArray();
            
            if (choice < 4) {
                scores.put(types[0], scores.getOrDefault(types[0], 0) + 4 - choice);
            } else {
                scores.put(types[1], scores.getOrDefault(types[1], 0) + choice - 4);   
            }
        }    
        
        return new StringBuilder()
            .append(scores.getOrDefault('R', 0) >= scores.getOrDefault('T', 0) ? 'R' : 'T')
            .append(scores.getOrDefault('C', 0) >= scores.getOrDefault('F', 0) ? 'C' : 'F')
            .append(scores.getOrDefault('J', 0) >= scores.getOrDefault('M', 0) ? 'J' : 'M')
            .append(scores.getOrDefault('A', 0) >= scores.getOrDefault('N', 0) ? 'A' : 'N')
            .toString();
    }
}