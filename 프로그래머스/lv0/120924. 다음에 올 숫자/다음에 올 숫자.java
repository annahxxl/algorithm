class Solution {
    public int solution(int[] common) {
        int n = common.length;
        
        int d = common[1] - common[0];
        if (common[2] - common[1] == d) return common[n - 1] + d;
        
        int r = common[1] / common[0];
        return common[n - 1] * r;
    }
}