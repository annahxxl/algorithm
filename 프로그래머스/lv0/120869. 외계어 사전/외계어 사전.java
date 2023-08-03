import java.util.*;

class Solution {
    public int solution(String[] spell, String[] dic) {
        int cnt = 0;
    
        for (String word : dic) {
            Map<String, Integer> spellMap = new HashMap<>();
            
            for (String key : spell) spellMap.put(key, 0);
        
            for (String s : word.split("")) {
                if (spellMap.containsKey(s)) {
                    spellMap.put(s, spellMap.get(s) + 1);
                }
            }

            boolean allOne = true;
            
            for (int value : spellMap.values()) {
                if (value != 1) {
                    allOne = false;
                    break;
                }
            }
            
            if (allOne) cnt++;
        }

        return cnt > 0 ? 1 : 2;
    }
}