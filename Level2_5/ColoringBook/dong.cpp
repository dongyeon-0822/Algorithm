#include <iostream>
#include <vector>
using namespace std;

int search(int m,int n,int i,int j, vector<vector<int>> &picture, int &count, int color) {
    if (picture[i][j] == 0 || picture[i][j] == -1 || picture[i][j] != color) return 0;
    else {
        picture[i][j] = -1;
        count++;
        if (i != 0) search(m, n, i - 1, j, picture, count, color);
        if (i + 1 != m) search(m, n, i + 1, j, picture, count, color);
        if (j != 0) search(m, n, i, j - 1, picture, count, color);
        if (j + 1 != n) search(m, n, i, j + 1, picture, count, color);
        return 1;
    }
}
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    int color, count;

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            count = 0;
            color = picture[i][j];
            if (search(m, n, i, j, picture, count, color))
                number_of_area++;
            if (count > max_size_of_one_area)
                max_size_of_one_area = count;
        }
    }
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}
int main() {
    vector<vector<int>> picture = { {1, 1, 1, 0},{1, 1, 1, 0},{0, 0, 0, 1},{0, 0, 0, 1},{0, 0, 0, 1},{0, 0, 0, 1} };
    solution(6, 4, picture);
    cout << solution;
}