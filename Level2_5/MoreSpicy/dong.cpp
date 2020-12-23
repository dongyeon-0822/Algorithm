#include <iostream>
#include <string>
#include <vector>
#include <queue>
using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    int new_scv, pop_1, pop_2;
    priority_queue< int, vector<int>, greater<int> > scv;
    for (int i = 0; i < scoville.size(); i++) {
        scv.push(scoville[i]);
    }
    while (1) {
        if (scv.top() > K || scv.size() == 1) break;
        pop_1 = scv.top();
        scv.pop();
        pop_2 = scv.top();
        scv.pop();
        new_scv = pop_1 + pop_2 * 2;
        scv.push(new_scv);
        answer++;
    }
    if (scv.top() < K) answer = -1;
    return answer;
}