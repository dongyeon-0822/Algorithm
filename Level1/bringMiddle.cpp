#include <iostream>
#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    int middle;
    if (s.size() % 2 == 0) {
        middle = s.size() / 2-1;
        answer += s.substr(middle, 2);
    }
    else {
        middle = s.size() / 2;
        answer += s[middle];
    }
    return answer;
}