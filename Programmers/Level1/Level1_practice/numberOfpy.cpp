#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    int p_count = 0;
    int y_count = 0;
    for (int i = 0; i < s.size(); i++) {
        s[i]=tolower(s[i]);
    }
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == 'p') p_count++;
        if (s[i] == 'y') y_count++;
    }
    if (p_count != y_count) answer = false;
    
    return answer;
}