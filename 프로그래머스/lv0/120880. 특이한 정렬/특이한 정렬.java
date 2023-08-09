import java.util.*;

class Solution {
    public int[] solution(int[] numlist, int n) {
        int[] answer = new int[numlist.length];
        double[] diff = new double[numlist.length];
        
        for(int i = 0; i < numlist.length; i++) {
            if(numlist[i] - n < 0) {
                diff[i] = Math.abs(numlist[i] - n) + 0.5;
            } else { 
                diff[i] = numlist[i] - n; 
            }
        }

        Arrays.sort(diff);
        
        for(int i = 0; i < numlist.length; i++) {
            if(diff[i] % 1 != 0) answer[i] = n - (int)diff[i];
            else answer[i] = (int)diff[i] + n;
        }
        
        return answer;
    }
}