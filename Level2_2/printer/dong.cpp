#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;

    queue<int> q;
    int max = *max_element(priorities.begin(), priorities.end());

    for (int i = 0; i < priorities.size(); i++) {
        q.push(i);
    }
    
    while (!q.empty()) {
        if (priorities[q.front()] != max) {
            q.push(q.front());
            q.pop();
        }
        else {
            answer++;
            if (q.front() == location) {
                break;
            }
            priorities[q.front()] = 0;
            q.pop();
            max = *max_element(priorities.begin(), priorities.end());
        }
        
    }
    
    return answer;
}