#include <iostream>
#include <string>
#include <cctype>
#include <deque>

using namespace std;

string solution(string new_id) {
    string answer = "";

    for (int i = 0; i < new_id.size(); i++)
        new_id[i] = tolower(new_id[i]);
    
    deque<char> str;
    for (int i = 0; i < new_id.size(); i++) {
        if (isdigit(new_id[i]) || islower(new_id[i]) || new_id[i] == '_' || new_id[i] == '-' || new_id[i] == '.') {
            if (str.empty() && new_id[i] == '.') continue;
            if (!str.empty() && str.back() == '.' && new_id[i] == '.') continue;
            str.push_back(new_id[i]);
        }
    }
    if (str.back() == '.') {
        str.pop_back();
    }
    if (str.empty()) str.push_back('a');
    if (str.size() <= 2) {
        char last = str.back();
        while (str.size() < 3) 
            str.push_back(last);
    }
    if (str.size() >= 16) {
        while (str.size() > 15)
            str.pop_back();
        if(str.back()=='.') str.pop_back();
    }
    for (int i = 0; i < str.size(); i++)
        answer += str[i];
    return answer;
}
int main() {
    cout << solution("...!@BaT#*..y.abcdefghijklm");
}