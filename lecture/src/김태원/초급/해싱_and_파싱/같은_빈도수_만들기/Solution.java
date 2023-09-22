package 김태원.초급.해싱_and_파싱.같은_빈도수_만들기;

import java.util.*;

class Solution {
    public int[] solution(String s) {
        Map<Character, Integer> map = new HashMap<>();

        for (char c : s.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }


        int max = Integer.MIN_VALUE;
        String strings = "abcde";

        for (char key : strings.toCharArray()) {
            if (map.getOrDefault(key, 0) > max) {
                max = map.getOrDefault(key, 0);
            }
        }

        int[] answer = new int[5];

        for (int i = 0; i < strings.length(); i++) {
            answer[i] = max - map.getOrDefault(strings.charAt(i), 0);
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution T = new Solution();
        System.out.println(Arrays.toString(T.solution("aaabc")));
        System.out.println(Arrays.toString(T.solution("aabb")));
        System.out.println(Arrays.toString(T.solution("abcde")));
        System.out.println(Arrays.toString(T.solution("abcdeabc")));
        System.out.println(Arrays.toString(T.solution("abbccddee")));
    }
}
