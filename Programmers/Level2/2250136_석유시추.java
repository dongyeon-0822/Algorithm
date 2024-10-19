import java.util.*;

class Solution {
    class Oil {
        int size;
        HashSet<Integer> cols;

        Oil(int size, HashSet<Integer> cols) {
            this.size = size;
            this.cols = cols;
        }
    }

    int[] dx = {-1, 1, 0, 0};
    int[] dy = {0, 0, -1, 1};
    boolean[][] visited;  // 동적으로 크기를 지정할 배열

    public int solution(int[][] land) {
        int N = land.length;   // 행 길이
        int M = land[0].length;  // 열 길이

        // 방문 배열을 동적으로 land의 크기에 맞게 초기화
        visited = new boolean[N][M];
        int[] answer = new int[M];  // 열에 따른 정답 배열

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                // land가 0이거나 이미 방문한 경우는 건너뜀
                if (land[i][j] == 0 || visited[i][j]) continue;

                HashSet<Integer> s = new HashSet<>();
                Oil newOil = new Oil(0, s);
                Oil o = dfs(newOil, i, j, land, N, M);  // 새로운 Oil 객체로 dfs 탐색
                for (Integer col : o.cols) {
                    answer[col] += o.size;  // 각 열에 크기 추가
                }
            }
        }

        // 최대값 반환
        return Arrays.stream(answer).max().orElse(0);
    }

    // dfs 탐색 메소드
    public Oil dfs(Oil o, int x, int y, int[][] arr, int n, int m) {
        if (visited[x][y]) return o;  // 이미 방문한 경우 종료
        visited[x][y] = true;  // 방문 처리
        o.size += 1;  // 크기 증가
        o.cols.add(y);  // 현재 열 추가

        // 상하좌우로 탐색
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            // 경계 조건 확인 및 방문 여부 확인
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny] && arr[nx][ny] == 1) {
                o = dfs(o, nx, ny, arr, n, m);  // 재귀 호출
            }
        }

        return o;
    }
}