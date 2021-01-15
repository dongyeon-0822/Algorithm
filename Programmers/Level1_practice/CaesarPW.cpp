#include <string>
#include <vector>
using namespace std;

string solution(string s, int n) {
    string answer = "";
    char c;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == ' ') answer += " ";
        else if (s[i] >= 'a' && s[i] <= 'z') {
            if (s[i] + n > 'z') {
                c = 'a' + s[i] + n - 'z'-1;
                answer += c;
            }
            else answer += s[i] + n;
        }
        else if (s[i] >= 'A' && s[i] <= 'Z') {
            if (s[i] + n > 'Z') {
                c = 'A' + s[i] + n - 'Z'-1;
                answer += c;
            }
            else answer += s[i] + n;
        }
    }
    return answer;
}