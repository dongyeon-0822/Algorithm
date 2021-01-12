#include <iostream>
#include <queue>

using namespace std;

int main() {
	int N;
	scanf("%d", &N);

	priority_queue<int,vector<int>,greater<int>> q;
	int num;
	for (int i = 0; i < N * N; i++) {
		scanf(" %d", &num);
		if (i < N) q.push(num);
		else if (i >= N && q.top() < num) {
			q.pop(); q.push(num);
		}
	}
	printf("%d", q.top());
}