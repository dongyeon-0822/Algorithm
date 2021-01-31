#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

class Node {
public:
	int data;
	vector<Node*> adj;
	bool visited;
	Node(int data) {
		this->data = data;
		visited = false;
	}
};
class Graph {
	vector<Node*> nodes;
public:
	void createNode(int size) {
		for (int i = 0; i < size; i++) {
			nodes.push_back(new Node(i));
		}
	}
	void addEdge(int n1, int n2) {
		Node* a = nodes[n1];
		Node* b = nodes[n2];
		if (find(a->adj.begin(), a->adj.end(), b) == a->adj.end()) {
			a->adj.push_back(b);
			b->adj.push_back(a);
		}
	}
	void search(int i,int &count) {
		Node* a = nodes[i];
		queue<Node*> q;

		a->visited = true;
		q.push(a);
		while (!q.empty()) {
			Node* temp = q.front();
			q.pop(); count++;
			for (int i = 0; i < temp->adj.size(); i++) {
				if (!temp->adj[i]->visited) {
					temp->adj[i]->visited = true;
					q.push(temp->adj[i]);
				}
			}
		}
	}
};
int main() {
	int comNum,link;
	scanf("%d", &comNum);
	scanf("%d", &link);

	Graph virus;
	virus.createNode(comNum);

	int a, b;
	for (int i = 0; i < link; i++) {
		scanf("%d %d", &a, &b);
		virus.addEdge(a - 1, b - 1);
	}
	int count = -1;
	virus.search(0, count);
	printf("%d", count);
}