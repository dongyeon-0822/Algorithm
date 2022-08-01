import java.util.*;

public class NumandAddDivisor {
	boolean num_divisor(int num) {
		double sqrt = Math.sqrt(num);
		if (sqrt == (int)sqrt)
			return true;
		else
			return false;
	}
	
	public int solution(int left, int right) {
        int answer = 0;
        for(int i = left; i<=right; i++) {
        	if(num_divisor(i))
        		answer -= i;
        	else
        		answer += i;
        }
        return answer;
    }
}
