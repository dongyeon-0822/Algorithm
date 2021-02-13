#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int arr[100][100] = { 0 };
int visited[100][100] = { 0 };

int search(int m, int n, int i, int j, int &count) {
	if (visited[i][j] || arr[i][j]) return 0;
	visited[i][j] = 1;
	count++;
	if (i != 0) search(m, n, i - 1, j, count);
	if (i != m - 1) search(m, n, i + 1, j, count);
	if (j != 0) search(m, n, i, j - 1, count);
	if (j != n - 1) search(m, n, i, j + 1, count);
	return 1;
}
int main() {
	int M, N, K;
	scanf("%d %d %d", &M, &N, &K);

	int x1, y1, x2, y2;
	for (int i = 0; i < K; i++) {
		scanf(" %d %d %d %d", &x1, &y1, &x2, &y2);
		for (int x = x1; x < x2; x++) {
			for (int y = y1; y < y2; y++) {
				arr[y][x] = 1;
			}
		}
	}

	vector<int> area;
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			int count = 0;
			if (search(M, N, i, j, count))
				area.push_back(count);
		}
	}
	sort(area.begin(), area.end());
	printf("%d\n", area.size());
	for (int i = 0; i < area.size(); i++) {
		printf("%d ", area[i]);
	}

	return 0;
}