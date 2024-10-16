import java.io.*;
import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int answer = 0;
        
        HashMap<String, Integer> relations = new HashMap<>();
        HashMap<String, Integer[]> giftScore = new HashMap<>();
        
        // gift -> 선물 지수 갱신 & 주고 받은 선물 갱신
        for (String gift : gifts) {
            relations.put(gift, relations.getOrDefault(gift, 0) + 1);
            
            String tmp[] = gift.split(" ");
            String giver = tmp[0];
            String taker = tmp[1];
            
            // 준 사람 + 1
            if (giftScore.containsKey(giver)) {
                Integer[] exScore = giftScore.get(giver);
                Integer[] newScore = {0,0,0};
                newScore[0] = exScore[0] + 1;
                newScore[1] = exScore[1];
                newScore[2] = newScore[0] - newScore[1];
                giftScore.put(giver, newScore);
            }
            else {
                Integer[] newScore = {1,0,0};
                giftScore.put(giver, newScore);
            }
            // 받은 사람 + 1
            if (giftScore.containsKey(taker)) {
                Integer[] exScore = giftScore.get(taker);
                Integer[] newScore = {0,0,0};
                newScore[0] = exScore[0];
                newScore[1] = exScore[1] + 1;
                newScore[2] = newScore[0] - newScore[1];
                giftScore.put(taker, newScore);
            }
            else {
                Integer[] newScore = {0,1,0};
                giftScore.put(taker, newScore);
            }   
        }
        
        HashMap<String, Integer> result = new HashMap<>();
        
        for (int i = 0; i < friends.length; i++) {
            for (int j = i+1; j < friends.length; j++){
                String giver = friends[i];
                String taker = friends[j];
                
                int given = relations.getOrDefault(giver + " " + taker, 0);
                int taken = relations.getOrDefault(taker + " " + giver, 0);
                if (given > taken){
                    result.put(giver, result.getOrDefault(giver, 0) + 1);
                }
                else if (given < taken){
                    result.put(taker, result.getOrDefault(taker, 0) + 1);
                }
                else {
                    int score_1 = 0;
                    int score_2 = 0;
                    if (giftScore.containsKey(giver)){
                        score_1 = giftScore.get(giver)[2];
                    }
                    if (giftScore.containsKey(taker)){
                        score_2 = giftScore.get(taker)[2];
                    }
                    
                    if (score_1 > score_2){
                        result.put(giver, result.getOrDefault(giver, 0) + 1);
                    }
                    else if (score_1 < score_2){
                        result.put(taker, result.getOrDefault(taker, 0) + 1);
                    }
                }
            }
        }
        for (Integer v : result.values()){
            if (v > answer) 
                answer = v;
        }
        
        return answer;
    }
}