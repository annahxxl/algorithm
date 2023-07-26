class Solution {
    public int solution(int num, int k) {
        String numStr = String.valueOf(num);
        for (int i = 0; i < numStr.length(); i++) {
            if (Integer.parseInt(String.valueOf(numStr.charAt(i))) == k) {
                return i + 1;
            }
        }
        return -1;
    }
}
