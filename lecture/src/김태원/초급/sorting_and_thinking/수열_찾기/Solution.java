package 김태원.초급.sorting_and_thinking.수열_찾기;

import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public int[] solution(int[] nums) {
        int n = nums.length;

        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num : nums) map.put(num, map.getOrDefault(num, 0) + 1);

        Arrays.sort(nums);

        int[] answer = new int[n / 2];
        int idx = 0;

        for (int num : nums) {
            if (map.get(num) == 0) continue;

            answer[idx] = num;
            idx++;

            map.put(num, map.get(num) - 1);
            map.put(num * 2, map.get(num * 2) - 1);

        }

        return answer;
    }

    public static void main(String[] args) {
        Solution T = new Solution();
        System.out.println(Arrays.toString(T.solution(new int[]{1, 10, 2, 3, 5, 6})));
        System.out.println(Arrays.toString(T.solution(new int[]{1, 1, 6, 2, 2, 7, 3, 14})));
        System.out.println(Arrays.toString(T.solution(new int[]{14, 4, 2, 6, 3, 10, 10, 5, 5, 7, 7, 14})));
    }
}
