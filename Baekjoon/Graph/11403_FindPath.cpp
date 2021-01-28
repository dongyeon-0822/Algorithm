#include <iostream>
#include <vector>
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
		if (find(a->adj.begin(), a->adj.end(), b) == a->adj.end())
			a->adj.push_back(b);
	}
	bool search(int i, int j) {
		Node* a = nodes[i];
		Node* b = nodes[j];

		for (int i = 0; i < nodes.size(); i++) //ÃÊ±âÈ­
			nodes[i]->visited = false;

		queue<Node*> q;
		a->visited = true;
		q.push(a);
		while (!q.empty()) {
			Node* temp = q.front();
			q.pop(); 
			for (int i = 0; i < temp->adj.size(); i++) {
				if (temp->adj[i] == b) return true;
				if (!temp->adj[i]->visited) {
					temp->adj[i]->visited = true;
					q.push(temp->adj[i]);
				}
			}
		}
		return false;
	}
};
int main() {
	Graph g;

	int N;
	scanf("%d", &N);
	g.createNode(N);

	int** arr;
	arr = new int* [N];
	for (int i = 0; i < N; i++)
		arr[i] = new int[N];
	
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			scanf(" %d", &arr[i][j]);
			if (arr[i][j] == 1) {
				g.addEdge(i, j);
			}
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (g.search(i, j)) printf("1 ");
			else printf("0 ");
		}printf("\n");
	}

	for (int i = 0; i < N; i++)
		delete[] arr[i];
	delete[] arr;
}