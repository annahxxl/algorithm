import java.util.*;

class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] words = {"aya", "ye", "woo", "ma"};

        for (String b : babbling) {
            for (String w : words) {
                b = b.replace(w, "-");
            }

            Set<Character> set = new HashSet<>();
            for (char c : b.toCharArray()) {
                set.add(c);
            }

            if (set.size() == 1 && set.contains('-')) {
                answer++;
            }
        }

        return answer;
    }
}