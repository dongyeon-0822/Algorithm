#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    multiset<string> set;
    vector<string>::iterator p;
    //insert
    for (p = participant.begin();p!= participant.end();p++) {
        set.insert(*p);
    }
    //search¿÷¿∏∏È erase
    for (int i = 0; i < completion.size(); i++) {
        set.erase(set.find(completion[i]));
    }
    answer += *set.begin();
    return answer;
}
int main() {
    vector<string> participant = { "leo", "kiki", "eden" };
    vector<string> completion = { "kiki","eden" };

    cout << solution(participant, completion);
}