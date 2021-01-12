#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
	int N, M;
	scanf("%d %d", &N, &M);
	
	vector<int> priority(N + 1, 0);
	vector<vector<int>> linked(N + 1);
	
	for (int i = 0; i < M; i++) {
		int a, b;
		scanf(" %d %d", &a, &b);
		linked[a].push_back(b);
		priority[b]++;
	}
	priority_queue<int,vector<int>,greater<int>> pq;
	for (int i = 1; i <= N; i++) {
		if (priority[i] == 0) 
			pq.push(i);
	}
	for (int i = 1; i <= N; i++) {
		int solve = pq.top();
		pq.pop();
		printf("%d ", solve);
		for (int j = 0; j < linked[solve].size(); j++) {
			if (--priority[linked[solve][j]] == 0)
				pq.push(linked[solve][j]);
		}
	}
}