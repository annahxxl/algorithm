import java.util.*;

class Solution {
    public String[] solution(String my_str, int n) {
        List<String> answer = new ArrayList<>();
        
        int strLen = my_str.length();
        
        for (int i = 0; i < strLen; i += n) {
            int endIdx = i + n;
                
            if (endIdx < strLen) {
                answer.add(my_str.substring(i, endIdx));
            } else {
                answer.add(my_str.substring(i));
            }
        }
        
        return answer.toArray(new String[0]);
    }
}