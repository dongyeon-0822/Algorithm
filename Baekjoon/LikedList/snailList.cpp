#include <iostream>
#include <vector>
using namespace std;

typedef struct node* np;
typedef struct node {
	int data;
	np next;
	node(int data) {
		this->data = data;
	}
}node;
np list[200000];

void addNode(np pre, np nn) {
	pre->next = nn;
	nn->next = NULL;
}
int main() {
	int N, M, V;
	scanf("%d %d %d", &N, &M, &V);

	int C;
	for (int i = 0; i < N; i++) {
		scanf(" %d", &C);
		list[i] = new node(C);
		if (i == 0) {
			list[i]->next = NULL;
		}
		else if (i == N - 1) {
			list[i - 1]->next = list[i];
			list[i]->next = list[V - 1];
		}
		else {
			addNode(list[i - 1], list[i]);
		}
	}

	int K;
	vector<int> arr_K;
	for (int i = 0; i < M; i++) {
		scanf(" %d", &K);
		arr_K.push_back(K);
	}

	
	for (int i = 0; i < M; i++) {
		int cycle= (N - V + 1);
		int index = arr_K[i];

		if (index < V-1) {
			printf("%d\n", list[index]->data);
		}
		else {
			printf("%d\n", list[(index - (V - 1)) % cycle + (V - 1)]->data);
		}
	}
}
