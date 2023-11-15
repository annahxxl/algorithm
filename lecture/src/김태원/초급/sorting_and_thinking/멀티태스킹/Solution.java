package 김태원.초급.sorting_and_thinking.멀티태스킹;

import java.util.*;
import java.util.stream.IntStream;

class Solution {
    public int solution(int[] tasks, long k) {

        int[] sortedTasks = IntStream.concat(IntStream.of(0), Arrays.stream(tasks).sorted()).toArray();

        int remainingTaskCnt = tasks.length; // for sortedTasks

        for (int i = 1; i < sortedTasks.length; i++) {
            long time = (long) remainingTaskCnt * (sortedTasks[i] - sortedTasks[i - 1]);

            if (time > k) {
                long lastTaskOrder = k % remainingTaskCnt;
                int notCompletedTaskCnt = 0; // for tasks

                for (int j = 0; j < tasks.length; j++) {
                    if (tasks[j] >= sortedTasks[i]) {
                        if (notCompletedTaskCnt == lastTaskOrder) {
                            return j + 1;
                        }
                        notCompletedTaskCnt++;
                    }
                }
            } else {
                remainingTaskCnt--;
                k -= time;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        Solution T = new Solution();
        System.out.println(T.solution(new int[]{1, 2, 3}, 5));
        System.out.println(T.solution(new int[]{8, 5, 2, 9, 10, 7}, 30));
        System.out.println(T.solution(new int[]{8, 9, 12, 23, 45, 16, 25, 50}, 100));
    }
}
