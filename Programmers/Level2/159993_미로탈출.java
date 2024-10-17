import java.util.*;

class Solution {
    int[] dx = {-1,1,0,0};
    int[] dy = {0,0,-1,1};
    int n;
    int m;
    
    class Info{
        int distance;
        int x;
        int y;
        
        Info(int distance, int x, int y){
            this.distance = distance;
            this.x = x;
            this.y = y;
        }
    }
    
    public int bfs(int startX, int startY, int endX, int endY, String[] maps) {
        Deque<Info> q = new ArrayDeque<>();
        boolean[][] visited = new boolean[n][m];
        
        q.addLast(new Info(0, startX, startY));
        visited[startX][startY] = true;
        while (!q.isEmpty()) {
            Info info = q.pollFirst();
            if (info.x == endX && info.y == endY){
                return info.distance;
            }
            for (int i = 0; i < 4; i++){
                int nx = info.x + dx[i];
                int ny = info.y + dy[i];
                
                if (0 > nx || nx >= n || 0 > ny || ny >= m) continue;
                if (maps[nx].charAt(ny) == 'X' || visited[nx][ny]) continue;
                q.addLast(new Info(info.distance + 1, nx, ny));
                visited[nx][ny] = true;
            }
        }
        return -1;
    }
    
    public int solution(String[] maps) {
        n = maps.length;
        m = maps[0].length();
            
        int sx = -1, sy = -1;
        int ex = -1, ey = -1;
        int lx = -1, ly = -1;
        
        
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (maps[i].charAt(j) == 'S'){
                    sx = i;
                    sy = j;
                }
                else if (maps[i].charAt(j) == 'E'){
                    ex = i;
                    ey = j;
                }
                else if (maps[i].charAt(j) == 'L'){
                    lx = i;
                    ly = j;
                }
            }
        }
        
        int distance_1 = bfs(sx, sy, lx, ly, maps);
        int distance_2 = bfs(lx, ly, ex, ey, maps);
        
        if (distance_1 == -1 || distance_2 == -1){
            return -1;
        }
        return distance_1 + distance_2;
    }
}