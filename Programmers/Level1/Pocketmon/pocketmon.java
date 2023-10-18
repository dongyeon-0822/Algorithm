import java.util.*;


class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        HashMap<Integer, Integer> h = new HashMap<>();
        for (int num : nums){
            h.put(num, 0);
        }
        if (h.size() >= nums.length / 2){
            answer = (int) nums.length;
        } else {
            answer = h.size();
        }
        return answer;
    }
}