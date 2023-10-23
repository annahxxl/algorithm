package 김태원.초급.해싱_and_시간파싱.문서_도난;

import java.util.*;

class Info implements Comparable<Info> {
    public String name;
    public int minutes;

    public Info(String name, int minutes) {
        this.name = name;
        this.minutes = minutes;
    }

    @Override
    public int compareTo(Info info) {
        return minutes - info.minutes;
    }
}

class Solution {
    private int convertToMinutes(String time) {
        int h = Integer.parseInt(time.split(":")[0]);
        int m = Integer.parseInt(time.split(":")[1]);
        return h * 60 + m;
    }

    public String[] solution(String[] reports, String times) {
        List<Info> infos = new ArrayList<>();

        for (String report : reports) {
            String name = report.split(" ")[0];
            String time = report.split(" ")[1];
            infos.add(new Info(name, convertToMinutes(time)));
        }

        Collections.sort(infos);

        int start = convertToMinutes(times.split(" ")[0]);
        int end = convertToMinutes(times.split(" ")[1]);

        List<String> answer = new ArrayList<>();

        for (Info info : infos) {
            if (info.minutes >= start && info.minutes <= end) {
                answer.add(info.name);
            }
        }

        return answer.toArray(new String[0]);
    }

    public static void main(String[] args) {
        Solution T = new Solution();
        System.out.println(Arrays.toString(T.solution(new String[]{"john 15:23", "daniel 09:30", "tom 07:23", "park 09:59", "luis 08:57"}, "08:33 09:45")));
        System.out.println(Arrays.toString(T.solution(new String[]{"ami 12:56", "daniel 15:00", "bob 19:59", "luis 08:57", "bill 17:35", "tom 07:23", "john 15:23", "park 09:59"}, "15:01 19:59")));
        System.out.println(Arrays.toString(T.solution(new String[]{"cody 14:20", "luis 10:12", "alice 15:40", "tom 15:20", "daniel 14:50"}, "14:20 15:20")));
    }
}
