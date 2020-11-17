#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <queue>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> days;
    int count = 0;

    for (int i = 0; i < progresses.size(); i++) {
        int day = ceil((float)(100 - progresses[i]) / speeds[i]);

        if (days.empty()) {
            days.push_back(day); count++;
        }
        else {
            if (days[0] < day) {
                answer.push_back(count);
                days.clear(); 
                days.push_back(day);
                count = 1;
            }
            else {
                days.push_back(day); count++;
            }
        }
    }
    answer.push_back(count);
    return answer;
}
int main() {
    solution({ 93,30,55 }, { 1,30,5 });
    cout << endl;
    solution({ 95,90,99,99,80,99 }, { 1,1,1,1,1,1 });
}