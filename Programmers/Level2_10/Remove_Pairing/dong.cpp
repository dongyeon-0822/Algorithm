#include <iostream>
#include <deque>
#include <string>
using namespace std;

int solution(string s)
{
    int answer = 0;
    deque<char> dq;
    
    for (int i = 0; i < s.size(); i++) {
        if (dq.empty()) {
            dq.push_back(s[i]); continue;
        }
        if (dq.back() == s[i]) dq.pop_back();
        else dq.push_back(s[i]);
    }
    if (dq.empty()) answer = 1;
    return answer;
}
int main() {
    cout << solution("cdcd");
}