package week11.day4;

import java.util.PriorityQueue;

public class Programmers_138477 {
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];
        PriorityQueue<Integer> priorityQueueLowest = new PriorityQueue<>();

        for (int i = 0; i < score.length; i++) {
            priorityQueueLowest.add(score[i]);
            if (priorityQueueLowest.size() > k)
                priorityQueueLowest.poll();
            answer[i] = priorityQueueLowest.peek();
        }

        return answer;
    }
}
