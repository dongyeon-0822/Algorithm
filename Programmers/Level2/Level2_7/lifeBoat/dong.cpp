#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;

    sort(people.begin(), people.end());
    
    int min = 0;
    int max = people.size() - 1;
    while (1) {
        if (min > max) break;
        if (min == max) { 
            answer++; break;
        }
        if (people[min] + people[max] <= limit) {
            max--; min++;
            answer++;
        }
        else {
            max--;
            answer++;
        }
    }
    return answer;
}
int main() {
    vector<int> people = { 70,50,80,50 };
    cout << solution(people, 100);
}