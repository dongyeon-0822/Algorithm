#include <iostream>
#include <cmath>
using namespace std;

void hanoi(int n, int start,int via,int end) {
	if (n == 1) {
		printf("%d %d\n", start, end);
	}
	else {
		hanoi(n - 1, start, end, via);
		printf("%d %d\n", start, end);
		hanoi(n - 1, via, start, end);
	}
}
int main() {
	int N;
	cin >> N;

	printf("%d\n", (int)pow(2, N) - 1);
	hanoi(N, 1, 2, 3);
}