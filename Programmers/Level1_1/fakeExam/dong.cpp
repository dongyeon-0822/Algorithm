#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> count(3);

    int stu1[] = { 1,2,3,4,5 };
    int stu2[] = { 2,1,2,3,2,4,2,5 };
    int stu3[] = { 3,3,1,1,2,2,4,4,5,5 };

    for (int i = 0; i < answers.size(); i++) {
        if (answers[i] == stu1[i % 5]) count[0]++;
        if (answers[i] == stu2[i % 8]) count[1]++;
        if (answers[i] == stu3[i % 10]) count[2]++;
    }
    int arr[3] = { count[0],count[1],count[2] };
    sort(arr, arr + 3);
    int max = arr[2];

    for (int i = 0; i < 3; i++) {
        if (max == count[i])
            answer.push_back(i + 1);
    }

    return answer;
}
int main() {
    vector<int> answers = { 1,2,3,4,5 };
}