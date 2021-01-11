#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

void add_node(int K, int level, int first, int last, vector<int> node, vector<vector<int>> &tree) {
	if (first <= last && K >= level) {
		int index = (last - first) / 2 + first;
		tree[level].push_back(node[index]);
		add_node(K, level + 1, first, index - 1, node, tree);
		add_node(K, level + 1, index + 1, last, node, tree);
	}
}
int main() {
	int K;
	cin >> K;

	vector<vector<int>> tree(K);
	vector<int> node;
	int n;
	for (int i = 0; i < pow(2, K) - 1; i++) {
		scanf_s(" %d", &n);
		node.push_back(n);
	}
	int level = 0;
	add_node(K, level, 0, node.size() - 1, node, tree);
	for (int i = 0; i < K; i++) {
		for (int j = 0; j < (int)pow(2, i); j++) {
			printf("%d ", tree[i][j]);
		}printf("\n");
	}
}