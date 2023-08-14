class Solution {
    public int solution(String A, String B) {
        if (A.equals(B)) return 0;
        
        String str = A;
        for (int i = 0; i < A.length(); i++) {
            str = str.charAt(str.length() - 1) + str.substring(0, str.length() - 1);
            if (str.equals(B)) return i + 1;
        }
        
        return -1;
    }
}