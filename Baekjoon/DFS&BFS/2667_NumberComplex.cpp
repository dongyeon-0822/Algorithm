#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int visited[25][25] = { 0, };

int DFS(int i, int j,int &N,int &count,int **arr) {
	if (visited[i][j] == 1 || arr[i][j] == 0) return 0;
	
	visited[i][j] = 1;
	count++;
	if (i != 0) DFS(i - 1, j, N, count, arr);
	if (i != N - 1) DFS(i + 1, j, N, count, arr);
	if (j != 0) DFS(i, j - 1, N, count, arr);
	if (j != N - 1) DFS(i, j + 1, N, count, arr);
	return 1;
}
int main() {
	int N;
	scanf("%d", &N);

	int** arr;
	arr = new int* [N];
	for (int i = 0; i < N; i++)
		arr[i] = new int[N];

	char s[26];
	for (int i = 0; i < N; i++) {
		scanf("%s", s);
		for (int j = 0; j < N; j++) {
			arr[i][j] = (s[j] - 48);
		}
	}

	vector<int> complex;
	int complexNum = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			int count = 0;
			if (DFS(i, j, N, count, arr)) {
				complex.push_back(count);
				complexNum++;
			}
		}
	}
	sort(complex.begin(), complex.end());

	printf("%d\n", complexNum);
	for (int i = 0; i < complex.size(); i++) 
		printf("%d\n", complex[i]);
}