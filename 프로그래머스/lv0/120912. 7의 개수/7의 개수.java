class Solution {
    public int solution(int[] array) {
        int answer = 0;
        
        for (int num :  array) {
            String str = String.valueOf(num);
            for (char c : str.toCharArray()) {
                if (c == '7') answer++;
            }
        }
        
        return answer;
    }
}