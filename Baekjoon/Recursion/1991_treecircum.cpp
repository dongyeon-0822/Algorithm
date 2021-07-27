#include <iostream>
#include <vector>
using namespace std;

class node {
public:
	char value;
	node* left;
	node* right;
	node() { value = ' '; left = NULL; right = NULL; }
};

void preorder(node* node) {
	if (node != NULL) {
		printf("%C", node->value);
		preorder(node->left);
		preorder(node->right);
	}
}
void inorder(node* node) {
	if (node != NULL) {
		inorder(node->left);
		printf("%C", node->value);
		inorder(node->right);
	}
}
void postorder(node* node) {
	if (node != NULL) {
		postorder(node->left);
		postorder(node->right);
		printf("%C", node->value);
	}
}
int main() {
	int num_node;
	cin >> num_node;

	node* n = new node[num_node];
	for (int i = 0; i < num_node; i++) {
		char value, left, right;
		cin >> value >> left >> right;
		n[value - 'A'].value = value;
		if (left != '.') n[value - 'A'].left = &n[left - 'A'];
		else n[value - 'A'].left = NULL;
		if (right != '.')n[value - 'A'].right = &n[right - 'A'];
		else n[value - 'A'].right = NULL;
	}
	preorder(&n[0]);
	printf("\n");
	inorder(&n[0]);
	printf("\n");
	postorder(&n[0]);
	printf("\n");
}