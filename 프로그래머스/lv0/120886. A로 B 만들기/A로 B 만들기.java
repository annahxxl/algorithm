import java.util.*;

class Solution {
    public int solution(String before, String after) {
        if (before.length() != after.length()) return 0;

        char[] beforeChars = before.toCharArray();
        char[] afterChars = after.toCharArray();

        Arrays.sort(beforeChars);
        Arrays.sort(afterChars);

        return Arrays.equals(beforeChars, afterChars) ? 1 : 0;
    }
}