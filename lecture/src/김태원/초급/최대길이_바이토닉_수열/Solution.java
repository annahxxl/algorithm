package 김태원.초급.최대길이_바이토닉_수열;

import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int n = nums.length;
        List<Integer> peakIndices = new ArrayList<>();

        for (int i = 1; i < n - 1; i++) {
            if (nums[i - 1] < nums[i] && nums[i] > nums[i + 1]) {
                peakIndices.add(i);
            }
        }

        for (int peakIdx : peakIndices) {
            int leftIdx = peakIdx;
            int rightIdx = peakIdx;
            int cnt = 1;

            while (leftIdx - 1 >= 0 && nums[leftIdx - 1] < nums[leftIdx]) {
                cnt++;
                leftIdx--;
            }

            while (rightIdx + 1 < n && nums[rightIdx] > nums[rightIdx + 1]) {
                cnt++;
                rightIdx++;
            }

            answer = Math.max(answer, cnt);
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution T = new Solution();
        System.out.println(T.solution(new int[]{1, 2, 1, 2, 3, 2, 1}));
        System.out.println(T.solution(new int[]{1, 1, 2, 3, 5, 7, 4, 3, 1, 2}));
        System.out.println(T.solution(new int[]{3, 2, 1, 3, 2, 4, 6, 7, 3, 1}));
        System.out.println(T.solution(new int[]{1, 3, 1, 2, 1, 5, 3, 2, 1, 1}));
    }
}
