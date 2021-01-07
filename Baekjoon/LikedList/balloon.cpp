#include <iostream>
using namespace std;

typedef struct node* np;
typedef struct node{
	int data;
	int index;
	np right;
	np left;
	node(int data, int index) {
		this->data = data;
		this->index = index;
	}
}node;

void addNode(np pre, np nn) {
	nn->left = pre;
	nn->right = pre->right;
	pre->right->left = nn;
	pre->right = nn;
}
void removeNode(np remove) {
	printf("%d ", remove->index);
	remove->left->right = remove->right;
	remove->right->left = remove->left;
}
np temp,temp1;
int value;
void right_remove(int num) {
	temp = temp1;
	for (int i = 0; i < num; i++) {
		temp = temp->right;
	}
	value = temp->data;
	temp1 = temp->left;
	removeNode(temp);
}
void left_remove(int num) {
	temp = temp1;
	for (int i = 0; i < num; i++) {
		temp = temp->left;
	}
	value = temp->data;
	temp1 = temp->left;
	removeNode(temp);
}
int main() {
	int n;
	cin >> n;
	
	np list[1000];
	int data;
	for (int i = 0; i < n; i++) {
		cin >> data;
		list[i] = new node(data, i + 1);
		if (i == 0) { //첫번째 노드일 때
			list[i]->left = list[i];
			list[i]->right = list[i];
		}
		else {
			addNode(list[i - 1], list[i]);
		}
	}
	value = list[0]->data;
	temp1 = list[0]->left;
	removeNode(list[0]); //첫번째 풍선 터트리기
	for (int i = 1; i < n; i++) {
		if (value > 0)
			right_remove(value);
		else
			left_remove(-value-1);
	}
}