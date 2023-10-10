package 김태원.초급.자료구조_활용.최대_길이_연속수열;

import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] nums) {
//        Set<Integer> setNums = new HashSet<>();
//        for (int num : nums) setNums.add(num);
        Set<Integer> setNums = Arrays.stream(nums).boxed().collect(Collectors.toSet());
        int answer = 0;

        for (int num : setNums) {
            if (setNums.contains(num - 1)) continue;

            int cnt = 0;
            while (setNums.contains(num++)) cnt++;

            answer = Math.max(answer, cnt);
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution T = new Solution();
        System.out.println(T.solution(new int[]{8, 1, 9, 3, 10, 2, 4, 0, 2, 3}));
        System.out.println(T.solution(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0}));
        System.out.println(T.solution(new int[]{3, 3, 3, 3, 3, 3, 3, 3}));
        System.out.println(T.solution(new int[]{-3, -1, -2, 0, 3, 3, 5, 6, 2, 2, 1, 1}));
        System.out.println(T.solution(new int[]{-5, -3, -1, -4, 3, 3, 5, 6, 2, 2, 1, 1, 7}));
    }
}