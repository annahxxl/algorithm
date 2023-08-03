class Solution {
    public int solution(String my_string) {
        int answer = 0;
        String numStr = "0";
        
        for (char c : my_string.toCharArray()) {
            if (Character.isDigit(c)) {
                numStr += c;
                continue;
            }
            
            answer += Integer.parseInt(numStr);
            numStr = "0";
        }
        
        answer += Integer.parseInt(numStr);
        
        return answer;
    }
}