#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer(2, 0);
    map<string, int> m;

    char first, end;
    m[words[0]] = 0;
    for (int i = 1; i < words.size(); i++) {
        first = words[i][0];
        end = words[i - 1][words[i - 1].size() - 1];
        if (m.find(words[i]) != m.end() || first != end) {
            answer[0] = i % n + 1;
            answer[1] = i / n + 1;
            return answer;
        }else m[words[i]] = i;
    }
    return answer;
}
int main() {
    vector<string> words = { "a", "aba", "aba","a" };
    vector<int> sol = solution(4, words);
    for (int i = 0; i < sol.size(); i++) {
        cout << sol[i];
    }
}