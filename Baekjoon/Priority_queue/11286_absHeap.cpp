#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct cmp {
	bool operator()(int a,int b){
		if (abs(a) == abs(b))
			return a > b;
		else return abs(a) > abs(b);
	}
};
int main() {
	int N;
	scanf("%d", &N);

	vector<int> arr;
	for (int i = 0; i < N; i++) {
		int n;
		scanf(" %d", &n);
		arr.push_back(n);
	}
	priority_queue<int, vector<int>, cmp> abs_heap;
	for (int i = 0; i < arr.size(); i++) {
		if (arr[i] == 0) {
			if (abs_heap.empty())
				printf("0\n");
			else {
				printf("%d\n", abs_heap.top());
				abs_heap.pop();
			}
		}
		else abs_heap.push(arr[i]);
	}
	
}