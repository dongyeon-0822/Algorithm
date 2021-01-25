#include <iostream>
#include <queue>
#include <vector>
#include <cstring>
using namespace std;

bool isPrime[10000];

int BFS(int a,int b) {
	bool visited[10000] = { false }; //초기화
	int level[10000] = { 0 }; //초기화
	queue<int> q;

	q.push(a);
	visited[a] = true;

	while (!q.empty()) {
		int tmp = q.front();
		q.pop();

		if (tmp == b) {
			return level[tmp];
		}
		for (int i = 0; i < 4; i++) {
			int n[4];
			n[0] = tmp % 10;
			n[1] = (tmp / 10) % 10;
			n[2] = (tmp / 100) % 10;
			n[3] = tmp / 1000;
			for (int j = 0; j < 10; j++) {
				if (i == 3 && j == 0) continue;
				n[i] = j;
				int num = n[0] + n[1] * 10 + n[2] * 100 + n[3] * 1000;
				if (isPrime[num] && !visited[num]) {
					q.push(num);
					visited[num] = true;
					level[num] = level[tmp] + 1;
				}
			}
		}
	}
	return -1;
}

int main() {
	int T;
	scanf("%d", &T);

	//소수판별
	memset(isPrime, true, sizeof(isPrime));
	for (int i = 2; i * i <= 10000; i++) {
		if (!isPrime[i]) continue;
		for (int j = i * i; j < 10000; j += i)
			isPrime[j] = false;
	}

	vector<int> answer;
	for (int i = 0; i < T; i++) {
		int a, b;
		scanf(" %d %d", &a, &b);
		answer.push_back(BFS(a, b));
	}
	for (int i = 0; i < answer.size(); i++) {
		printf("%d\n", answer[i]);
	}
}