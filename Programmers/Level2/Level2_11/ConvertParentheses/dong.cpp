#include <string>
#include <vector>
#include <queue>

using namespace std;

bool isCorrect(string s) {
    queue<char> q;
    
    for (int i = 0; i < s.size(); i++) {
        if (q.empty())
            q.push(s[i]);
        else {
            if (q.back() == '(' && s[i] == ')')
                q.pop();
            else q.push(s[i]);
        }
    }
    if (q.empty()) return true;
    else return false;
}
string divide(string w) {
    if (w == "") return ""; //1

    int cnt_1 = 0, cnt_2 = 0;
    string u = "", v = "";
    for (int i = 0; i < w.size(); i++) { //2
        if (w[i] == '(') cnt_1++;
        else cnt_2++;
        if (cnt_1 == cnt_2) {
            u = w.substr(0, i + 1);
            v = w.substr(i + 1);
            break;
        }
    }
    if (isCorrect(u)) { //3
        return u + divide(v);
    }
    else { //4
        string s = "";
        s = "(" + divide(v) + ")";
        for (int i = 1; i < u.size() - 1; i++) {
            if (u[i] == '(') s += ")";
            else s += "(";
        }
        return s;
    }
}
string solution(string p) {
    if(isCorrect(p)) return p;
    return divide(p);
}