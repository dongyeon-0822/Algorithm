#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    vector<int> stu(n, 1);

    for (int i = 0; i < lost.size(); i++) {
        stu[lost[i] - 1]--;
    }
    for (int i = 0; i < reserve.size(); i++) {
        stu[reserve[i] - 1]++;
    }

    for (int i = 0; i < n; i++) {
        //왼쪽사람 빌려주기
        if (i != 0 && stu[i - 1] == 0 && stu[i] == 2) {
            stu[i - 1]++; stu[i]--;
        }
        //오른쪽사람 빌려주기
        if (i != n-1 && stu[i] == 2 && stu[i+1] == 0) {
            stu[i]--; stu[i+1]++;
        }
    }
    
    for (int i = 0; i < n; i++) {
        if (stu[i] == 1) answer++;
    }

    return answer;
}