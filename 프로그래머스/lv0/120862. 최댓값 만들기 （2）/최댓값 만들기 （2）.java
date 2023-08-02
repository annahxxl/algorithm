class Solution {
    public int solution(int[] numbers) {
        int answer = Integer.MIN_VALUE;
        int len = numbers.length;
        
        for (int i = 0; i < len; i++) {
            for (int j = i + 1; j < len; j++) {
                answer = Math.max(answer, numbers[i] * numbers[j]);
            }
        }
        
        return answer;
    }
}