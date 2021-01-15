#include <iostream>
#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    int index = 0;
    for (int i = 0; i < s.size(); i++, index++) {
        if (s[i] == ' ') { 
            index = -1; 
            answer += " "; 
        }
        else {
            if (index % 2 == 0) 
                answer += toupper(s[i]);
            else if (index % 2 == 1)
                answer += tolower(s[i]);
        }
    }
    return answer;
}