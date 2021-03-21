#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> solution(vector<string> orders, vector<int> course) {
    vector<string> answer;

	// 1���� 6���� ���� ����
	vector<int> n;

	// 1���� 6���� ����
	for (int i = 0; i < 6; i++) {
		n.push_back(i + 1);
	}

	// 0��1�� ���� �� ���� ����
	vector<int> ind;

	// k=4, 4���� �����ϱ�
	int k = 4;

	// k���� 1 �߰�
	for (int i = 0; i < k; i++) {
		ind.push_back(1);
	}

	// 2��(6��-2��)�� 0 �߰�
	for (int i = 0; i < n.size() - k; i++) {
		ind.push_back(0);
	}

	// ����
	sort(ind.begin(), ind.end());

	//����
	do {
		// ���

		for (int i = 0; i < ind.size(); i++) {
			if (ind[i] == 1) {
				printf("%d ", n[i]);
			}
		}

		printf("\n");

	} while (next_permutation(ind.begin(), ind.end()));

    return answer;
}