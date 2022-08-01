import java.util.*;

public class Marathon {
	public String solution(String[] participant, String[] completion) {
        Arrays.sort(participant);
        Arrays.sort(completion);
        int i;
        for(i = 0; i<completion.length; i++) {
        	if (!participant[i].equals(completion[i]))
        		return participant[i];
        }
        return participant[i];
    }
	
	public static void main(String[] args) {
		Marathon m = new Marathon();
		String[] participant = {"marina", "josipa", "nikola", "vinko", "filipa"};
		String[] completion = {"josipa", "filipa", "marina", "nikola"};
		String s = m.solution(participant,completion);
        System.out.println(s);  // 스태틱 메서드는 클래스를 이용하여 호출
    }
}
