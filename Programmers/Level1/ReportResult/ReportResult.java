import java.util.*;

public class ReportResult {
	public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        int[] num = new int[id_list.length];
        HashSet<String> rp = new HashSet<>(Arrays.asList(report));
        ArrayList<String> result = new ArrayList<>();
        
        for(String s : rp) {
        	num[Arrays.asList(id_list).indexOf(s.split(" ")[1])]++;
        }
        for(int i = 0; i < id_list.length; i++) {
        	if(num[i] >= k)
        		result.add(id_list[i]);
        }
        for(String s : rp) {
        	if (result.contains(s.split(" ")[1]))
        		answer[Arrays.asList(id_list).indexOf(s.split(" ")[0])]++;
        }
        return answer;
    }
	
	public static void main(String[] args) {
		ReportResult m = new ReportResult();
		String[] id_list = {"muzi", "frodo", "apeach", "neo"};
		String[] report = {"muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"};
		int[] s = m.solution(id_list,report,2);
        // System.out.println(s);  // 스태틱 메서드는 클래스를 이용하여 호출
    }
}
