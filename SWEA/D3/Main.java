import java.util.*;
import java.io.*;

public class Main {
    static HashMap<Integer, int[]> dic = new HashMap<>();
    static ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
    static boolean[] visited;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = 1;
        int row = 0;
        while (n <= 10000) {
            ArrayList<Integer> line = new ArrayList<>();
            int col = 0;
            while (col <= row) {
                dic.put(n, new int[]{row, col});
                line.add(n);
                n++;
                col++;
            }
            row++;
            arr.add(line);
        }

        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            visited = new boolean[100001];
            String[] input = br.readLine().split(" ");
            int s = Integer.parseInt(input[0]);
            int e = Integer.parseInt(input[1]);
            int start = Math.min(s, e);
            int end = Math.max(s, e);

            Queue<int[]> q = new LinkedList<>();
            q.offer(new int[]{start, 0});
            visited[start] = true;
            int answer = 0;
            
            while (!q.isEmpty()) {
                int[] current = q.poll();
                int x = dic.get(current[0])[0];
                int y = dic.get(current[0])[1];
                int d = current[1];
                
                if (arr.get(x).get(y) == end) {
                    answer = d;
                    break;
                }
                
                int[][] directions = {{0, -1}, {0, 1}, {1, 0}, {1, 1}};
                for (int[] direction : directions) {
                    int nx = x + direction[0];
                    int ny = y + direction[1];
                    if (0 <= ny && ny <= nx && nx < 140 && !visited[arr.get(nx).get(ny)]) {
                        q.offer(new int[]{arr.get(nx).get(ny), d + 1});
                        visited[arr.get(nx).get(ny)] = true;
                    }
                }
            }
            System.out.println("#" + t + " " + answer);
        }
    }
}
