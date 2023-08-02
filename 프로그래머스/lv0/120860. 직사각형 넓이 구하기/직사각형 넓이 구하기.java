import java.util.*;

class Solution {
    public int solution(int[][] dots) {
        int answer = 0;
        
        Set<Integer> xSet = new HashSet<>();
        Set<Integer> ySet = new HashSet<>();
        
        for (int[] dot : dots) {
            xSet.add(dot[0]);
            ySet.add(dot[1]);
        }
        
        List<Integer> xList = new ArrayList<>(xSet);
        List<Integer> yList = new ArrayList<>(ySet);
        
        return Math.abs((xList.get(0) - xList.get(1)) * (yList.get(0) - yList.get(1)));
    }
}