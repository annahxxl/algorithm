package 김태원.초급.해싱_and_시간파싱.서로_다른_빈도수_만들기;

import java.util.*;

class Solution {
    public int solution(String s) {
        Map<Character, Integer> map = new HashMap<>();

        for (char c : s.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }

        Set<Integer> set = new HashSet<>();
        int answer = 0;

        for (char key : map.keySet()) {
            while (set.contains(map.get(key))) {
                answer++;
                map.put(key, map.get(key) - 1);
            }

            if (map.get(key) == 0) continue;

            set.add(map.get(key));
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution T = new Solution();
        System.out.println(T.solution("aaabbbcc"));
        System.out.println(T.solution("aaabbc"));
        System.out.println(T.solution("aebbbbc"));
        System.out.println(T.solution("aaabbbcccde"));
        System.out.println(T.solution("aaabbbcccdddeeeeeff"));
    }
}
