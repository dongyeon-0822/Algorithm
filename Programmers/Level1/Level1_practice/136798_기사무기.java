package week11.day4;

import java.util.ArrayList;
import java.util.List;

public class Programmers_136798 {
    static int numOfDivisor(int n) {
        int num = 2;
        for (int i = 2; i < (int)Math.sqrt(n)+1; i++)
            if (n % i == 0)
                num+=2;
        if (Math.sqrt(n) % 1 == 0) {
            num--;
        }
        return num;
    }
    public int solution(int number, int limit, int power) {
        int answer = 0;
        List<Integer> list = new ArrayList<>();
        for (int i = 1; i <= number; i++) {
            int x = numOfDivisor(i);
            if (x > limit)
                list.add(power);
            else
                list.add(x);
        }
        for (Integer n : list) {
            answer += n;
        }
        return answer;
    }
}
