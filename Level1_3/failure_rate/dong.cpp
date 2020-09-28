#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    vector<int> no_clear(N + 1);
    vector<int> clear(N);
    vector<double> f_rate(N);
    vector<double> arr(N);

    //�� �������� no_clear�� player �� 
    for (int i = 0; i < stages.size(); i++) {
        no_clear[stages[i] - 1]++;
    }
    //�� ���������� clear�� player ��
    int sum = 0;
    for (int i = N ; i > 0 ; i--) {
        sum += no_clear[i];
        clear[i - 1] = sum;
    }
    //�� ���������� ������
    for (int i = 0; i < N; i++) {
        if (no_clear[i] == 0)
            f_rate[i] = 0.0;
        else 
            f_rate[i] = (double)no_clear[i] / ((double)no_clear[i] + (double)clear[i]);
        
    }
    //���纻�� ����� ����
    arr.assign(f_rate.begin(), f_rate.end());
    sort(arr.begin(), arr.end());
    for (int i = N-1; i >= 0 ; i--) {
        for (int j = 0; j < N; j++) {
            if (arr[i] == f_rate[j]) {
                answer.push_back(j + 1);
                f_rate[j] = -1;
            }
        }
    }
    return answer;
}
int main() {
    vector<int> stages = { 2,1,2,6,2,4,3,3 };
    solution(5, stages);
}